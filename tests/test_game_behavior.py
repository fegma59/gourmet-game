from unittest import TestCase
from gourmet_game.game_behavior import BehaviorFactory, SmartBehavior, DefaultBehavior


class TestBehaviorFactory(TestCase):
    def test_load_behavior(self):
        object_to_test = BehaviorFactory()
        assert isinstance(object_to_test, BehaviorFactory)


class TestSmartBehavior:
    def test_behavior(self):
        object_to_test = SmartBehavior()
        assert isinstance(object_to_test, SmartBehavior)


class TestDefaultBehavior:
    def test_fail_guess(self):
        object_to_test = DefaultBehavior()
        assert isinstance(object_to_test, DefaultBehavior)


    def test_behavior(self):
        object_to_test = DefaultBehavior()
        assert isinstance(object_to_test, DefaultBehavior)
