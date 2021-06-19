from gourmet_game.layout_factory import LayoutFactory
import PySimpleGUI as simplegui
from logs.setup_log import logger
import sys
from gourmet_game.dataset_singleton import GameDataSet
from gourmet_game.views import Views
class GourmetGame:
    def __init__(self):
        self.layout_factory = LayoutFactory()
        self.game_dataset = GameDataSet()
        self.views = Views()

    def if_guess(self):
        win_page_layout = self.layout_factory.create_window('StartContent', 'Ganheide novo!')
        win_page = self.views.view('Win', win_page_layout)
        return win_page

    def fail_guess(self, food, food_type, type):
        get_what_user_thought_layout = self.layout_factory.create_window('TextQuestion', 'Qual comida você pensou?')
        user_thought = self.views.view('Get User Thoght', get_what_user_thought_layout)['values']['answer']
        if type == 'same_type':
            phrase = f'{user_thought} e {food} são do tipo {food_type}.'
        else:
            phrase = f'{user_thought} é ________ mas {food} não.'
        get_phrase_complete_layout = self.layout_factory.create_window('StartContent',
                                                                       phrase)
        phrase_complete_view = self.views.view('Complete the Phrase', get_phrase_complete_layout)
        pass

    def run(self):
        logger.info("Gourmet Game Running!")
        while True:
            first_page_layout = self.layout_factory.create_window('StartContent', 'Pense em uma comida')
            index_view = self.views.view('Index', first_page_layout)
            if index_view['events'] == 'Ok':
                food_type = self.game_dataset.get_afood_type()
                get_tip_page_layout = self.layout_factory.create_window('BooleanQuestion', f'A comida que você pensou foi do tipo {food_type}')
                is_food_by_type_view = self.views.view('Get a Tip', get_tip_page_layout)
                if is_food_by_type_view['events'] == 'Sim':
                    food = self.game_dataset.get_afood_from_atype(food_type)
                    try_to_guess_page_layout = self.layout_factory.create_window('BooleanQuestion', f'A comida que você pensou foi a {food}')
                    guess = self.views.view('Try a guess', try_to_guess_page_layout)
                    if guess['events'] == 'Sim':
                        self.if_guess()
                    else:
                        self.fail_guess(food, food_type, 'same_type')
                elif is_food_by_type_view['events'] == 'Não':
                    food = self.game_dataset.get_afood_from_another_type(food_type)
                    try_to_guess_page_layout = self.layout_factory.create_window('BooleanQuestion',
                                                                                 f'A comida que você pensou foi a {food}')
                    guess = self.views.view('Try a guess', try_to_guess_page_layout)
                    if guess['events'] == 'Sim':
                        self.if_guess()
                    else:
                        self.fail_guess(food, food_type, 'other_type')
            elif index_view['events'] == 'Close':
                sys.exit(0)

if __name__ == "__main__":
    app = GourmetGame()
    app.run()