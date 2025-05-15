import unittest
from src.game_logic.word_manager import WordManager

class TestWordManager(unittest.TestCase):

    def setUp(self):
        self.word_manager = WordManager()
        self.word_manager.add_word("car", "Automobile")
        self.word_manager.add_word("dog", "Animal")
        self.word_manager.add_word("carrot", "Vegetable")

    def test_select_word(self):
        word = self.word_manager.select_word()
        self.assertIn(word, ["car", "dog", "carrot"])

    def test_add_new_word(self):
        self.word_manager.add_word("plane", "Automobile")
        self.assertIn("plane", self.word_manager.words["Automobile"])

    def test_categorize_new_word(self):
        self.word_manager.add_word("elephant", "Animal")
        self.assertIn("elephant", self.word_manager.words["Animal"])

    def test_word_count(self):
        self.assertEqual(len(self.word_manager.words["Automobile"]), 1)
        self.assertEqual(len(self.word_manager.words["Animal"]), 1)
        self.assertEqual(len(self.word_manager.words["Vegetable"]), 1)

if __name__ == '__main__':
    unittest.main()