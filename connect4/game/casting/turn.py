from game.shared.point import Point
from game.casting.actor import Actor


class Turn(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        self._turn = 0
        self._font_size = 15
        self._position = Point(10, 5)
        self.show_turn()
        
    def set_turn(self, turn):
        """Set the current turn number

        Args:
            turn (number): Turn number
        """
        self._turn = turn
        self.show_turn()
        
    def get_turn(self):
        """Return the current turn number

        Returns:
            int: Turn number
        """
        
        return self._turn

    def show_turn(self):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        if(self._turn % 2 == 0):
            self.set_text("Player One's turn")
        else:
            self.set_text("Player Two's turn")
