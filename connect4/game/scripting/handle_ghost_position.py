from game.scripting.action import Action
from game.shared.point import Point
import constants


class HandleGhostPosition(Action):
    """
        Handle ghost position in the board.
    """

    def __init__(self) -> None:
        self._block_positions = []

    def execute(self, cast, script):
        """
        ghost = cast.get_first_actor("ghost")
        p1_pieces = cast.get_actors("p1_pieces")
        p2_pieces = cast.get_actors("p2_pieces")
        max_y = Point(0, constants.ROWS).scale(constants.CELL_SIZE).get_y()
        print(len(self._block_positions))
        for piece in p1_pieces:
            if ghost.get_position().equals(piece.get_position()):
                if ghost.get_position().equalsToAny(self._block_positions) == False:
                    self._block_positions.append(ghost.get_position())

        for piece in p2_pieces:
            if ghost.get_position().equals(piece.get_position()):
                if ghost.get_position() not in self._block_positions:
                    self._block_positions.append(ghost.get_position())

        if ghost.get_position().equalsToAny(self._block_positions):
            self._direction = Point(0, -constants.CELL_SIZE)
            ghost.set_velocity(self._direction)
            ghost.move_next()
        else:
            self._direction = Point(0, constants.CELL_SIZE)
            ghost.set_velocity(self._direction)
            if ghost.get_next_position().get_y() <= max_y and ghost.get_next_position().equalsToAny(self._block_positions) == False:
                ghost.move_next()
                """
