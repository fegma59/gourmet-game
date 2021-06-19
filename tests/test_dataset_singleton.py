import unittest
import mock
import PySimpleGUI

from gourmet_game.dataset_singleton import GameDataSet

class TestLayoutFactory(unittest.TestCase):

    def test_get_afood_type(self):
        object_totest = GameDataSet()
        self.assertEqual(type(object_totest.get_afood_type()), type("<class 'str'>"))
        self.assertIsInstance(object_totest, GameDataSet)

    def test_get_afood_from_atype(self):
        object_totest = GameDataSet()
        self.assertEqual(type(object_totest.get_afood_from_atype('massas')), type("<class 'str'>"))
        self.assertIsInstance(object_totest, GameDataSet)

    def test_get_afood_from_atype(self):
        object_totest = GameDataSet()
        self.assertEqual(type(object_totest.get_afood_from_another_type('massas')), type("<class 'str'>"))
        self.assertIsInstance(object_totest, GameDataSet)

if __name__ == '__name__':
    unittest.main()