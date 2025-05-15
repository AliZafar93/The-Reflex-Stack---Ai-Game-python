class AIBot:
    def __init__(self, word_manager):
        self.word_manager = word_manager
        self.knowledge_base = {
            'Automobile': [],
            'Animal': [],
            'Vegetable': []
        }

    def learn_new_word(self, word, category):
        if category in self.knowledge_base:
            self.knowledge_base[category].append(word)

    def categorize_word(self, word):
        # Simple categorization logic based on known words
        for category, words in self.knowledge_base.items():
            if word in words:
                return category
        return None  # If the word is unknown

    def adapt_to_new_words(self):
        # This method can be called to update the AI's knowledge base with new words
        for word in self.word_manager.get_new_words():
            category = self.word_manager.get_category(word)
            if category:
                self.learn_new_word(word, category)