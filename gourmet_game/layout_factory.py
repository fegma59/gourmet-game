import PySimpleGUI as simplegui
from abc import ABCMeta, abstractmethod
from logs.setup_log import logger

class LayoutWindow(metaclass=ABCMeta):
    def __init__(self, question):
        self.question = question
        self.theme = simplegui.theme('Reddit')

    @abstractmethod
    def page_content(self):
        pass

class StartContent(LayoutWindow):
    def page_content(self):
        self.layout = [
            [simplegui.Text(self.question)],
            [simplegui.Button('Ok'), simplegui.Button('Close')],
        ]
        return self.layout


class BooleanQuestion(LayoutWindow):
    def page_content(self):
        self.layout = [
            [simplegui.Text(self.question)],
            [simplegui.Button('Sim'), simplegui.Button('Não')],
        ]
        return self.layout

class TextQuestion(LayoutWindow):
    def page_content(self):
        self.layout = [
            [simplegui.Text(self.question)],
            [simplegui.Input(key='answer')],
            [simplegui.Button('Ok')],
        ]
        return self.layout


class LayoutFactory:
    def create_window(self, object_type, question):
        logger.info('Creating gui template')
        return eval(object_type)(question).page_content()