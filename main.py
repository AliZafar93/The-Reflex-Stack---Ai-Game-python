#Ai Game: Reflex Game
#Ali Zafar [221443]
#Shumail Ali [221479]
import tkinter as tk
from tkinter import messagebox
import random
import time
import threading
import nltk
from nltk.corpus import wordnet as wn

# Download required NLTK resources
nltk.download('wordnet')
nltk.download('omw-1.4')

# Expanded Word Database
word_database = {
    "automobile": ["car", "truck", "ferrari", "cycle", "bmw", "audi", "bus", "motorbike", "van", "scooter"],
    "animal": ["cat", "dog", "tiger", "horse", "elephant", "giraffe", "zebra", "goat", "bear", "monkey", "kangaroo"],
    "vegetable": [ "potato", "tomato", "onion", "lettuce", "spinach", "broccoli", "pepper", "cabbage", "cucumber", "radish"]
}

# Classification using WordNet with fallback
def classify_word(word):
    word = word.lower()
    synsets = wn.synsets(word)

    # Check WordNet synsets for classification
    if synsets:
        for syn in synsets:
            for hypernym in syn.hypernyms():
                name = hypernym.name().lower()
                if "animal" in name or "mammal" in name or "bird" in name:
                    return "animal"
                elif "vegetable" in name or "plant" in name or "edible_fruit" in name or "edible_vegetable" in name:
                    return "vegetable"
                elif "vehicle" in name or "automobile" in name or "car" in name:
                    return "automobile"

    # Fallback keywords for classification
    categories = {
        "automobile": ["car", "truck", "bike", "motorcycle", "cycle", "scooter", "bicycle", "submarine"],
        "animal": ["dog", "cat", "elephant", "tiger", "horse", "goat", "cow", "rabbit", "wolf", "bear", "monkey", "parrot"],
        "vegetable": [ "onion", "spinach", "lettuce", "potato", "broccoli", "tomato", "pepper", "cucumber", "radish", "rose"]
    }

    for category, keywords in categories.items():
        if word in keywords:
            return category

    return "unknown"


def get_word_category(word):
    synsets = wn.synsets(word, pos=wn.NOUN)
    if not synsets:
        return None  # Word not found in WordNet

    # Define target categories and their corresponding keywords
    categories = {
        'automobile': ['vehicle', 'car', 'automobile'],
        'animal': ['animal', 'mammal', 'reptile', 'bird'],
        'vegetable': ['vegetable', 'plant', 'edible_plant']
    }

    # Analyze hypernyms of each synset
    for syn in synsets:
        hypernyms = syn.hypernym_paths()
        for path in hypernyms:
            for hyper in path:
                for category, keywords in categories.items():
                    if any(keyword in hyper.name().lower() for keyword in keywords):
                        return category
    return None  # No matching category found

# Game Class
class ReflexGame:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Reflex Game with WordNet")
        self.new_words = []
        self.classified_new_words = {}
        self.user_stacks = {"automobile": [], "animal": [], "vegetable": []}
        self.ai_stacks = {"automobile": [], "animal": [], "vegetable": []}
        self.correct_user = 0
        self.correct_ai = 0
        self.current_word_index = 0
        self.current_word = ""
        self.user_results = {}
        self.ai_results = {}
        self.game_words = []
        self.create_word_input_screen()

    def create_word_input_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text="Enter 5 New Words (Unseen by AI):").pack()
        self.entries = [tk.Entry(self.root) for _ in range(5)]
        for entry in self.entries:
            entry.pack()
        tk.Button(self.root, text="Classify & Start Game", command=self.classify_and_confirm_words).pack()
        tk.Label(self.root, text="Controls: 1 = Automobile | 2 = Animal | 3 = Vegetable").pack()

    # In classify_and_confirm_words, store the classified categories for new words
    def classify_and_confirm_words(self):
        self.new_words = [e.get().strip() for e in self.entries if e.get().strip()]
        if len(self.new_words) != 5:
            messagebox.showerror("Error", "Please enter exactly 5 words.")
            return

        # Use get_word_category to classify words
        self.classified_new_words = {}
        for word in self.new_words:
            category = get_word_category(word)
            if category:
                self.classified_new_words[word] = category
                # Dynamically update the word_database
                word_database.setdefault(category, []).append(word)
            else:
                self.classified_new_words[word] = "unknown"

        unknown_words = [word for word, cat in self.classified_new_words.items() if cat == "unknown"]
        self.new_words = [word for word in self.new_words if self.classified_new_words[word] != "unknown"]

        if not self.new_words:
            messagebox.showerror("Error", "All entered words are unrecognized. Try different ones.")
            return

        result_window = tk.Toplevel(self.root)
        result_window.title("Classification Results")
        for word in self.new_words:
            cat = self.classified_new_words[word]
            tk.Label(result_window, text=f"{word} → {cat.title()}").pack()
        if unknown_words:
            tk.Label(result_window, text="--- Unknown Words ---", fg="red").pack()
            for word in unknown_words:
                tk.Label(result_window, text=word, fg="red").pack()
        tk.Button(result_window, text="Start Game", command=lambda: [result_window.destroy(), self.start_game()]).pack()

    def start_game(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Ensure user-entered words are added first
        self.game_words = self.new_words[:]

        # Collect all database words excluding user-entered words
        remaining_words = [
            word for category in word_database.values() for word in category
            if word not in self.new_words
        ]

        # Add 5 random words from the remaining database words
        db_words = random.sample(remaining_words, min(5, len(remaining_words)))

        # Combine user-entered words with random database words
        self.game_words += db_words

        # Shuffle the final list of game words
        random.shuffle(self.game_words)
        self.current_word_index = 0

        self.create_game_ui()
        self.root.bind("<Key>", self.handle_keypress)
        threading.Thread(target=self.play_words_sequence).start()

    def create_game_ui(self):
        self.status_label = tk.Label(self.root, text="Get Ready!", font=("Arial", 14, "bold"))
        self.status_label.pack()

        self.word_label = tk.Label(self.root, text="", font=("Arial", 24))
        self.word_label.pack(pady=10)

        frame = tk.Frame(self.root)
        frame.pack(pady=5)

        self.user_labels = {}
        user_frame = tk.LabelFrame(frame, text="You", padx=10, pady=5)
        user_frame.grid(row=0, column=0, padx=20)
        for i, cat in enumerate(["automobile", "animal", "vegetable"]):
            tk.Label(user_frame, text=cat.title()).grid(row=0, column=i)
            lst = tk.Listbox(user_frame, height=10, width=15)
            lst.grid(row=1, column=i)
            self.user_labels[cat] = lst

        self.ai_labels = {}
        ai_frame = tk.LabelFrame(frame, text="AI Bot", padx=10, pady=5)
        ai_frame.grid(row=0, column=1, padx=20)
        for i, cat in enumerate(["automobile", "animal", "vegetable"]):
            tk.Label(ai_frame, text=cat.title()).grid(row=0, column=i)
            lst = tk.Listbox(ai_frame, height=10, width=15)
            lst.grid(row=1, column=i)
            self.ai_labels[cat] = lst

        tk.Label(self.root, text="Controls: 1 = Automobile | 2 = Animal | 3 = Vegetable").pack(pady=5)

    def play_words_sequence(self):
        while self.current_word_index < len(self.game_words):
            word = self.game_words[self.current_word_index]
            self.current_word = word
            self.word_label.config(text=word)

            ai_guess = self.ai_classify_with_mistake(word)
            if ai_guess in self.ai_stacks:
                self.ai_stacks[ai_guess].append(word)
                self.ai_labels[ai_guess].insert(tk.END, word)

            correct_cat = self.get_correct_category(word)
            self.ai_results[word] = (ai_guess == correct_cat)

            time.sleep(1)  # <-- Reduce this value for faster word appearance
            self.current_word_index += 1

        self.end_game()

    def ai_classify_with_mistake(self, word):
        correct_category = classify_word(word)
        if random.random() < 0.2:  # 20% chance to make a mistake
            wrong_categories = [cat for cat in ["automobile", "animal", "vegetable"] if cat != correct_category]
            return random.choice(wrong_categories)
        return correct_category

    def handle_keypress(self, event):
        key_map = {"1": "automobile", "2": "animal", "3": "vegetable"}
        if event.char in key_map and self.current_word_index < len(self.game_words):
            cat = key_map[event.char]
            word = self.current_word
            self.user_stacks[cat].append(word)
            self.user_labels[cat].insert(tk.END, word)
            correct_cat = self.get_correct_category(word)
            self.user_results[word] = (cat == correct_cat)

    # In get_correct_category, always use self.classified_new_words for new words
    def get_correct_category(self, word):
        # Check if the word exists in the database
        for cat, words in word_database.items():
            if word in words:
                return cat
        # Use the classified category for new words
        return self.classified_new_words.get(word, "unknown")

    # In end_game, count only unique correct answers
    def end_game(self):
        self.root.unbind("<Key>")

        # Recalculate correct answers based on the game_words order.
        correct_user = 0
        correct_ai = 0
        for word in self.game_words:
            if self.user_results.get(word, False):
                correct_user += 1
            if self.ai_results.get(word, False):
                correct_ai += 1

        if correct_user > correct_ai:
            result = "You Win!"
        elif correct_ai > correct_user:
            result = "AI Wins!"
        else:
            result = "Draw!"

        self.status_label.config(text=f"{result} (You: {correct_user}, AI: {correct_ai})")
        self.word_label.config(text="Game Over!")

        # Highlight results for user words
        for cat, lst in self.user_labels.items():
            for i in range(lst.size()):
                word = lst.get(i)
                lst.itemconfig(i, {'fg': 'green' if self.user_results.get(word, False) else 'red'})

        # Highlight results for AI words
        for cat, lst in self.ai_labels.items():
            for i in range(lst.size()):
                word = lst.get(i)
                lst.itemconfig(i, {'fg': 'green' if self.ai_results.get(word, False) else 'red'})


# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = ReflexGame(root)
    root.mainloop()
