import constants

from game.casting.cast import Cast
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.handle_ghost_position import HandleGhostPosition
from game.scripting.handle_pieces_position import HandlePiecesPosition
from game.casting.turn import Turn
from game.scripting.handle_turns import HandleTurns
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point
from game.casting.ghost import Ghost


def main():

    # create the cast
    cast = Cast()
    cast.add_actor("ghost", Ghost())
    cast.add_actor("turn", Turn())

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService(True)

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("input", HandleTurns(keyboard_service))
    script.add_action("update", HandleGhostPosition())
    script.add_action("update", HandlePiecesPosition())
    script.add_action("output", DrawActorsAction(video_service))

    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()
