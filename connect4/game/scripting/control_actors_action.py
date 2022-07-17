import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the ghost.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._velocity = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        ghost = cast.get_first_actor("ghost")
        
        # left
        if self._keyboard_service.is_key_down('a'):
            self._velocity = Point(-constants.CELL_SIZE, 0)
            ghost.set_velocity(self._velocity)
            ghost.move_next()
        # right
        if self._keyboard_service.is_key_down('d'):
            self._velocity = Point(constants.CELL_SIZE, 0)
            ghost.set_velocity(self._velocity)
            ghost.move_next()