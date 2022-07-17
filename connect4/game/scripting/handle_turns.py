import constants
from game.scripting.action import Action
from game.casting.piece import Piece
from game.shared.point import Point
from game.casting.actor import Actor


class HandleTurns(Action):
    """
    An input action that controls the action.

    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service) -> None:
        self._keyboard_service = keyboard_service
        self._execute = True
        self._turns = 0
        self._winner = None

    def execute(self, cast, script):
        """Executes the handle action action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        ghost = cast.get_first_actor("ghost")
        #   Check if there isn't winner
        if(self._winner == None):
            #   Run the play and Check Win functions.
            self.play(cast)
            self.check_win(cast)
        else:
            #   Makes ghost keep moving
            ghost.move_next()

            # Display game over and winner messages
            x = int(constants.MAX_X / 2)
            y = int(10)
            position = Point(x, y)
            message = Actor()
            message.set_font_size(30)
            message.set_text("Game Over!")
            message.set_position(position)
            message.set_color(constants.WHITE)
            cast.add_actor("messages", message)

            x = int(constants.MAX_X / 2)
            y = int(40)
            position = Point(x, y)

            winner = Actor()
            winner.set_position(position)
            if self._winner == "p1":
                winner.set_text("Winner: Player One")
                winner.set_color(constants.PLAYER1)
            else:
                winner.set_text("Winner: Player Two")
                winner.set_color(constants.PLAYER2)
            winner.set_font_size(30)
            cast.add_actor("messages", winner)

    def play(self, cast):
        ghost = cast.get_first_actor("ghost")
        p1_pieces = cast.get_actors("p1_pieces")
        p2_pieces = cast.get_actors("p2_pieces")
        turn = cast.get_first_actor("turn")

        if(self._keyboard_service.is_key_down("K")):
            if(self._execute == True):
                ghost.set_velocity(Point(0, constants.CELL_SIZE))
                if ghost.get_next_position().equalsToAny(p1_pieces) == False and ghost.get_next_position().equalsToAny(p2_pieces) == False:
                    if(self._turns % 2 == 0):
                        cast.add_actor("p1_pieces", Piece(
                            ghost.get_position(), constants.PLAYER1))
                    else:
                        cast.add_actor("p2_pieces", Piece(
                            ghost.get_position(), constants.PLAYER2))
                    self._turns += 1
                    turn.set_turn(self._turns)

                ghost.set_velocity(Point(constants.CELL_SIZE, 0))
                self._execute = False

        if(self._keyboard_service.is_key_up("K")):
            #   Reset the execution verification
            self._execute = True

    def check_win(self, cast):
        p1_pieces = cast.get_actors("p1_pieces")
        p2_pieces = cast.get_actors("p2_pieces")
        for piece in p1_pieces:
            if piece.get_falling() == False:
                # Horizontal
                # if piece next position is equal to any piece in the next 3 horizontal lines

                if(piece.get_next_position(Point(constants.CELL_SIZE, 0)).equalsToAny(p1_pieces) and
                    piece.get_next_position(Point(constants.CELL_SIZE * 2, 0)).equalsToAny(p1_pieces) and
                    piece.get_next_position(
                        Point(constants.CELL_SIZE * 3, 0)).equalsToAny(p1_pieces)
                   ):
                    self._winner = "p1"
                # Vertical
                # if piece next position is equal to any piece in the next 3 vertical lines
                
                if(piece.get_next_position(Point(0, constants.CELL_SIZE)).equalsToAny(p1_pieces) and
                    piece.get_next_position(Point(0, constants.CELL_SIZE * 2)).equalsToAny(p1_pieces) and
                    piece.get_next_position(
                        Point(0, constants.CELL_SIZE * 3)).equalsToAny(p1_pieces)
                   ):
                    self._winner = "p1"
                # Diagonal
                # if piece next position is equal to any piece in the next 3 diagonal lines
                
                if((piece.get_next_position(Point(-constants.CELL_SIZE, constants.CELL_SIZE)).equalsToAny(p1_pieces) and
                    piece.get_next_position(Point(-constants.CELL_SIZE * 2, constants.CELL_SIZE * 2)).equalsToAny(p1_pieces) and
                    piece.get_next_position(Point(-constants.CELL_SIZE * 3, constants.CELL_SIZE * 3)).equalsToAny(p1_pieces))
                    or
                    (piece.get_next_position(Point(-constants.CELL_SIZE, -constants.CELL_SIZE)).equalsToAny(p1_pieces) and
                     piece.get_next_position(Point(-constants.CELL_SIZE * 2, -constants.CELL_SIZE * 2)).equalsToAny(p1_pieces) and
                     piece.get_next_position(Point(-constants.CELL_SIZE * 3, -constants.CELL_SIZE * 3)).equalsToAny(p1_pieces))
                   ):
                    self._winner = "p1"

        for piece in p2_pieces:
            if piece.get_falling() == False:
                # Horizontal
                # if piece next position is equal to any piece in the next 3 horizontal lines

                if(piece.get_next_position(Point(constants.CELL_SIZE, 0)).equalsToAny(p2_pieces) and
                    piece.get_next_position(Point(constants.CELL_SIZE * 2, 0)).equalsToAny(p2_pieces) and
                    piece.get_next_position(
                        Point(constants.CELL_SIZE * 3, 0)).equalsToAny(p2_pieces)
                   ):
                    self._winner = "p2"

                # Vertical
                # if piece next position is equal to any piece in the next 3 vertical lines

                if(piece.get_next_position(Point(0, constants.CELL_SIZE)).equalsToAny(p2_pieces) and
                    piece.get_next_position(Point(0, constants.CELL_SIZE * 2)).equalsToAny(p2_pieces) and
                    piece.get_next_position(
                        Point(0, constants.CELL_SIZE * 3)).equalsToAny(p2_pieces)
                   ):
                    self._winner = "p2"

                # Diagonal
                # if piece next position is equal to any piece in the next 3 diagonal lines
                if((piece.get_next_position(Point(-constants.CELL_SIZE, constants.CELL_SIZE)).equalsToAny(p2_pieces) and
                    piece.get_next_position(Point(-constants.CELL_SIZE * 2, constants.CELL_SIZE * 2)).equalsToAny(p2_pieces) and
                    piece.get_next_position(Point(-constants.CELL_SIZE * 3, constants.CELL_SIZE * 3)).equalsToAny(p2_pieces))
                    or
                    (piece.get_next_position(Point(-constants.CELL_SIZE, -constants.CELL_SIZE)).equalsToAny(p2_pieces) and
                     piece.get_next_position(Point(-constants.CELL_SIZE * 2, -constants.CELL_SIZE * 2)).equalsToAny(p2_pieces) and
                     piece.get_next_position(Point(-constants.CELL_SIZE * 3, -constants.CELL_SIZE * 3)).equalsToAny(p2_pieces))
                   ):
                    self._winner = "p2"
