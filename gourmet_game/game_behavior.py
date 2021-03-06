from abc import ABCMeta, abstractmethod
from logs.setup_log import logger
import sys
from gourmet_game.dataset_singleton import GameDataSet
from gourmet_game.views import Views
from gourmet_game.layout_factory import LayoutFactory

class GameBehavior(metaclass=ABCMeta):
    def __init__(self):
        self.layout_factory = LayoutFactory()
        self.game_dataset = GameDataSet()
        self.views = Views()
        self.first_food = 'lasanha'
        self.second_food = 'bolo de chocolate'

    def if_guess(self):
        try:
            logger.info('Informing the user, Im the winner')
            win_page_layout = self.layout_factory.create_window('StartContent', 'Acertei de novo!')
            win_page = self.views.view('Win', win_page_layout)
            return win_page
        except Exception as exception_message:
            logger.error(f'Error to inform the winner - {exception_message}')
            sys.exit(0)
            pass

    def fail_guess(self, food, food_type, type):
        try:
            get_what_user_thought_layout = self.layout_factory.create_window('TextQuestion', 'Qual prato você pensou?')
            user_thought = self.views.view('Get User Thoght', get_what_user_thought_layout)['values']['answer']
            if type == 'same_type':
                phrase = f'{user_thought} e {food} são do tipo {food_type}.'
            else:
                phrase = f'{user_thought} é ________ mas {food} não.'
            get_phrase_complete_layout = self.layout_factory.create_window('TextQuestion',
                                                                           phrase)
            phrase_complete_view = self.views.view('Complete the Phrase', get_phrase_complete_layout)
            pass
        except Exception as exception_message:
            logger.error(f'Error in get the what user thougt - {exception_message}')
            pass

    @abstractmethod
    def behavior(self):
        pass

class DefaultBehavior(GameBehavior):
    def fail_guess(self, food, food_type, type):
        try:
            get_what_user_thought_layout = self.layout_factory.create_window('TextQuestion', 'Qual prato você pensou?')
            user_thought = self.views.view('Get User Thoght', get_what_user_thought_layout)['values']['answer']
            phrase = f'{user_thought} é ________ mas {food} não.'
            get_phrase_complete_layout = self.layout_factory.create_window('TextQuestion',
                                                                           phrase)
            phrase_complete_view = self.views.view('Complete the Phrase', get_phrase_complete_layout)
            pass
        except Exception as exception_message:
            logger.error(f'Error in get the what user thougt - {exception_message}')
            pass

    def behavior(self):
        while True:
            try:
                first_page_layout = self.layout_factory.create_window('StartContent', 'Pense em um prato que gosta')
                index_view = self.views.view('Index', first_page_layout)
                if index_view['events'] == 'Ok':
                    food_type = self.game_dataset.get_afood_type()
                    get_tip_page_layout = self.layout_factory.create_window('BooleanQuestion',
                                                                            f'O prato que você pensou é massa?')
                    is_food_by_type_view = self.views.view('Get a Tip', get_tip_page_layout)
                    if is_food_by_type_view['events'] == 'Sim':
                        logger.info('Right tip.')
                        food = self.first_food
                        try_to_guess_page_layout = self.layout_factory.create_window('BooleanQuestion',
                                                                                     f'O prato que você pensou é lasanha?')
                        guess = self.views.view('Try a guess', try_to_guess_page_layout)
                        if guess['events'] == 'Sim':
                            logger.info('Guessed!')
                            self.if_guess()
                        else:
                            logger.info('Wrong guess')
                            self.fail_guess(food, food_type, 'same_type')
                    elif is_food_by_type_view['events'] == 'Não':
                        logger.info('Wrong tip.')
                        food = self.second_food
                        try_to_guess_page_layout = self.layout_factory.create_window('BooleanQuestion',
                                                                                     f'A comida que você pensou foi a {food}')
                        guess = self.views.view('Try a guess', try_to_guess_page_layout)
                        if guess['events'] == 'Sim':
                            logger.info('Guessed!')
                            self.if_guess()
                        else:
                            logger.info('Wrong guess.')
                            self.fail_guess(food, food_type, 'other_type')
                elif index_view['events'] == 'Close':
                    sys.exit(0)
            except Exception as exception_message:
                logger.error(f'Gourmet Game shutting down - {exception_message}')
                sys.exit(0)

class SmartBehavior(GameBehavior):
    def behavior(self):
        while True:
            try:
                first_page_layout = self.layout_factory.create_window('StartContent', 'Pense em uma comida')
                index_view = self.views.view('Index', first_page_layout)
                if index_view['events'] == 'Ok':
                    food_type = self.game_dataset.get_afood_type()
                    get_tip_page_layout = self.layout_factory.create_window('BooleanQuestion',
                                                                            f'A comida que você pensou foi do tipo {food_type}')
                    is_food_by_type_view = self.views.view('Get a Tip', get_tip_page_layout)
                    if is_food_by_type_view['events'] == 'Sim':
                        logger.info('Right tip.')
                        food = self.game_dataset.get_afood_from_atype(food_type)
                        try_to_guess_page_layout = self.layout_factory.create_window('BooleanQuestion',
                                                                                     f'A comida que você pensou foi a {food}')
                        guess = self.views.view('Try a guess', try_to_guess_page_layout)
                        if guess['events'] == 'Sim':
                            logger.info('Guessed!')
                            self.if_guess()
                        else:
                            logger.info('Wrong guess')
                            self.fail_guess(food, food_type, 'same_type')
                    elif is_food_by_type_view['events'] == 'Não':
                        logger.info('Wrong tip.')
                        food = self.game_dataset.get_afood_from_another_type(food_type)
                        try_to_guess_page_layout = self.layout_factory.create_window('BooleanQuestion',
                                                                                     f'A comida que você pensou foi a {food}')
                        guess = self.views.view('Try a guess', try_to_guess_page_layout)
                        if guess['events'] == 'Sim':
                            logger.info('Guessed!')
                            self.if_guess()
                        else:
                            logger.info('Wrong guess.')
                            self.fail_guess(food, food_type, 'other_type')
                elif index_view['events'] == 'Close':
                    sys.exit(0)
            except Exception as exception_message:
                logger.error(f'Gourmet Game shutting down - {exception_message}')
                sys.exit(0)


class BehaviorFactory:
    def load_behavior(self, object_type:"Game Mode"):
        logger.info(f'Loading Behavior {object_type} Mode')
        return eval(object_type)().behavior()