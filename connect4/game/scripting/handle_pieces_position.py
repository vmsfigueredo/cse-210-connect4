from game.scripting.action import Action
from game.shared.point import Point
import constants
class HandlePiecesPosition(Action):
    """
        Handle ghost position in the board.
    """
    def __init__(self) -> None:
        self._block_positions = []
    
    def execute(self, cast, script):
        p1_pieces = cast.get_actors("p1_pieces")
        p2_pieces = cast.get_actors("p2_pieces")
        max_y = Point(0, constants.ROWS).scale(constants.CELL_SIZE).get_y()
        for piece in p1_pieces:
            if piece.get_next_position().get_y() <= max_y and (piece.get_next_position().equalsToAny(p1_pieces) == False and piece.get_next_position().equalsToAny(p2_pieces) == False):
                piece.fall()
            else:
                piece.set_falling(False)

        for piece in p2_pieces:
            if piece.get_next_position().get_y() <= max_y and (piece.get_next_position().equalsToAny(p1_pieces) == False and piece.get_next_position().equalsToAny(p2_pieces) == False):
                piece.fall()
            else:
                piece.set_falling(False)