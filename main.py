from logs.setup_log import logger
from gourmet_game.game_behavior import GameBehavior
from gourmet_game.game_behavior import BehaviorFactory
import sys
class GourmetGame:
    def __init__(self, mode='DefaultBehavior'):
        self.game_mode = mode

    def run(self):
        try:
            logger.info("Gourmet Game Running!")
            game = BehaviorFactory()
            game.load_behavior(self.game_mode)
        except Exception as exception_message:
            logger.error(f"Error to load game behavior - {exception_message}")
            sys.exit()


if __name__ == "__main__":
    app = GourmetGame()
    app.run()