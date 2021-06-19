from gourmet_game.layout_factory import LayoutFactory
import PySimpleGUI as simplegui

class GourmetGame:
    def run(self):
        factory = LayoutFactory()
        layout = factory.create_window('TextQuestion', 'Qual comida voce pensou?')
        janela = simplegui.Window('Tela de inicio', layout)
        while True:
            eventos, valores = janela.read()
            if eventos == simplegui.WINDOW_CLOSED:
                break
            if eventos == 'Ok':
                print(eventos)

if __name__ == "__main__":
    app = GourmetGame()
    app.run()