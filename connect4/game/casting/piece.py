from game.casting.actor import Actor
import constants
import random
import time
from game.shared.point import Point


class Piece(Actor):
    """
    A tasty item that snakes like to eat.

    The responsibility of Piece is to select a random position and points that it's worth.

    Attributes:
        _points (int): The number of points the food is worth.
    """

    def __init__(self, position, color):
        "Constructs a new Piece."
        super().__init__()
        self._points = 0
        self.set_text("@")
        self.set_color(color)
        self.set_position(position)
        self._falling = True
        self.fall()

    def get_points(self):
        """Gets the points the food is worth.

        Returns:
            points (int): The points the food is worth.
        """
        return self._points

    def get_falling(self):
        return self._falling

    def set_falling(self, falling):
        self._falling = falling

    def fall(self):
        self._velocity = Point(0, constants.CELL_SIZE)
        self.move_next()
