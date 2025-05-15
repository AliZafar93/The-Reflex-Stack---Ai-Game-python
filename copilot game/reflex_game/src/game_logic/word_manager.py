class WordManager:
    def __init__(self):
        self.word_database = {
            'Automobile': ['car', 'truck', 'bicycle', 'motorcycle'],
            'Animal': ['dog', 'cat', 'elephant', 'tiger'],
            'Vegetable': ['carrot', 'broccoli', 'spinach', 'potato']
        }
        self.new_words = {
            'Automobile': [],
            'Animal': [],
            'Vegetable': []
        }

    def get_random_words(self, category, count=5):
        import random
        words = self.word_database.get(category, [])
        return random.sample(words, min(count, len(words)))

    def add_new_word(self, category, word):
        if category in self.word_database:
            self.word_database[category].append(word)
            self.new_words[category].append(word)

    def get_all_words(self):
        all_words = []
        for category, words in self.word_database.items():
            all_words.extend(words)
        return all_words

    def categorize_word(self, word):
        for category, words in self.word_database.items():
            if word in words:
                return category
        return None

    def get_new_words(self, category):
        return self.new_words.get(category, [])