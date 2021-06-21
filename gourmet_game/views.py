from logs.setup_log import logger
import PySimpleGUI as simplegui
import sys
from gourmet_game.dataset_singleton import GameDataSet
from gourmet_game.layout_factory import LayoutFactory

class Views:
    def __init__(self):
        self.layout_factory = LayoutFactory()
        self.game_dataset = GameDataSet()

    def view(self, title, layout):
        try:
            logger.info('Creating a view based on a template')
            window = simplegui.Window(title, layout)
            events, values = window.read()
            if events == simplegui.WIN_CLOSED or events == 'Cancel':
                logger.info('User closed the game.')
                sys.exit(0)
            return {'events': events, 'values': values}
        except Exception as exception_message:
            logger.error(f'Creating view error - {exception_message}')
            sys.exit(0)

if __name__ == "__main__":
    app = Views()
    app.view()