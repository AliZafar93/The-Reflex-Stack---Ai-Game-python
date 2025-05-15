import unittest
from src.game_logic.ai_bot import AIBot
from src.game_logic.containers import Container

class TestAIBot(unittest.TestCase):
    def setUp(self):
        self.ai_bot = AIBot()
        self.container = Container()

    def test_categorize_word_automobile(self):
        self.container.add_word('car', 'Automobile')
        self.ai_bot.learn_new_word('car', 'Automobile')
        self.assertEqual(self.ai_bot.categorize_word('car'), 'Automobile')

    def test_categorize_word_animal(self):
        self.container.add_word('dog', 'Animal')
        self.ai_bot.learn_new_word('dog', 'Animal')
        self.assertEqual(self.ai_bot.categorize_word('dog'), 'Animal')

    def test_categorize_word_vegetable(self):
        self.container.add_word('carrot', 'Vegetable')
        self.ai_bot.learn_new_word('carrot', 'Vegetable')
        self.assertEqual(self.ai_bot.categorize_word('carrot'), 'Vegetable')

    def test_learn_new_word(self):
        self.ai_bot.learn_new_word('banana', 'Vegetable')
        self.assertEqual(self.ai_bot.categorize_word('banana'), 'Vegetable')

    def test_unknown_word(self):
        self.assertIsNone(self.ai_bot.categorize_word('unknown'))

if __name__ == '__main__':
    unittest.main()