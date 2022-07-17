from game.casting.actor import Actor
import constants
import random
from game.shared.point import Point


class Ghost(Actor):
    """
    A tasty item that snakes like to eat.

    The responsibility of Food is to select a random position and points that it's worth.

    Attributes:
        _points (int): The number of points the food is worth.
    """

    def __init__(self):
        "Constructs a new Food."
        super().__init__()
        self._points = 0
        self.set_text("@")
        self.set_color(constants.GREY)
        self.reset()

    def reset(self):
        """Selects a random position and points that the food is worth."""
        self._points = random.randint(1, 8)
        x = int(constants.COLUMNS / 2) - 1
        y = 0
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)
        self.set_position(position)

    def get_points(self):
        """Gets the points the food is worth.

        Returns:
            points (int): The points the food is worth.
        """
        return self._points
