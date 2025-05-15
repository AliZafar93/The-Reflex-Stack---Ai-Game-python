class Container:
    def __init__(self):
        self.categories = {
            "Automobile": [],
            "Animal": [],
            "Vegetable": []
        }

    def add_word(self, category, word):
        if category in self.categories:
            self.categories[category].append(word)
        else:
            raise ValueError("Invalid category. Choose from: Automobile, Animal, Vegetable.")

    def get_words(self, category):
        if category in self.categories:
            return self.categories[category]
        else:
            raise ValueError("Invalid category. Choose from: Automobile, Animal, Vegetable.")

    def get_all_words(self):
        return self.categories