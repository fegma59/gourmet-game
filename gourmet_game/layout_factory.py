import PySimpleGUI as simplegui
from abc import ABCMeta, abstractmethod

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
            [simplegui.Button('Ok')],
        ]
        return self.layout


class BoolQuestion(LayoutWindow):
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
        return eval(object_type)(question).page_content()



if __name__ == "__main__":
    factory = LayoutFactory()
    layout = factory.create_window('TextQuestion', 'Qual comida voce pensou?')
    janela = simplegui.Window('Tela de inicio', layout)
    while True:
        eventos, valores = janela.read()
        if eventos == simplegui.WINDOW_CLOSED:
            break
        if eventos == 'Ok':
            print(eventos)