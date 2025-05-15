import unittest
from src.game_logic.containers import Container

class TestContainer(unittest.TestCase):

    def setUp(self):
        self.container = Container()

    def test_add_word_to_automobile(self):
        self.container.add_word('Car', 'Automobile')
        self.assertIn('Car', self.container.automobile)

    def test_add_word_to_animal(self):
        self.container.add_word('Dog', 'Animal')
        self.assertIn('Dog', self.container.animal)

    def test_add_word_to_vegetable(self):
        self.container.add_word('Carrot', 'Vegetable')
        self.assertIn('Carrot', self.container.vegetable)

    def test_invalid_category(self):
        with self.assertRaises(ValueError):
            self.container.add_word('Unknown', 'UnknownCategory')

    def test_retrieve_words(self):
        self.container.add_word('Bicycle', 'Automobile')
        self.container.add_word('Cat', 'Animal')
        self.container.add_word('Lettuce', 'Vegetable')
        self.assertEqual(self.container.get_words('Automobile'), ['Bicycle'])
        self.assertEqual(self.container.get_words('Animal'), ['Cat'])
        self.assertEqual(self.container.get_words('Vegetable'), ['Lettuce'])

if __name__ == '__main__':
    unittest.main()