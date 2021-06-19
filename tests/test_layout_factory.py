import unittest
import mock
import PySimpleGUI

from gourmet_game.layout_factory import LayoutFactory

class TestLayoutFactory(unittest.TestCase):

    def test_LayoutFactory(self):
        object_totest = LayoutFactory()
        self.assertIsInstance(object_totest, LayoutFactory)

    def test_create_window_text_type_number_of_elements(self):
        object_totest = LayoutFactory().create_window('TextQuestion', 'Qual comida voce pensou?')
        number_of_elements = len(object_totest)
        self.assertEqual(number_of_elements, 3)

    def test_create_window_start_content_number_of_elements(self):
        object_totest = LayoutFactory().create_window('StartContent', 'Pense em um prato que gosta')
        number_of_elements = len(object_totest)
        self.assertEqual(number_of_elements, 2)

    def test_create_window_boolean_question_number_of_elements(self):
        object_totest = LayoutFactory().create_window('StartContent', 'O prato que você pensou, é uma massa?')
        number_of_elements = len(object_totest)
        self.assertEqual(number_of_elements, 2)

if __name__ == '__name__':
    unittest.main()