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

# Word database
word_database = {
    "automobile": ["car", "truck", "ferrari", "cycle", "BMW"],
    "animal": ["cat", "dog", "lion", "tiger", "horse"],
    "vegetable": ["carrot", "potato", "tomato", "onion", "lettuce"]
}

# Classification using WordNet
def classify_word(word):
    word = word.lower()
    synsets = wn.synsets(word)

    if not synsets:
        return "unknown"

    for syn in synsets:
        for hypernym in syn.hypernyms():
            name = hypernym.name().lower()
            if "animal" in name or "mammal" in name:
                return "animal"
            elif "vegetable" in name or "plant" in name or "edible_fruit" in name or "edible_vegetable" in name:
                return "vegetable"
            elif "vehicle" in name or "automobile" in name or "car" in name:
                return "automobile"

    # Fallback keyword-based check
    categories = {
        "automobile": ["car", "truck", "bike", "motorcycle", "jeep", "cycle"],
        "animal": ["dog", "cat", "lion", "elephant", "tiger", "horse", "goat", "cow", "rabbit", "wolf", "bear"],
        "vegetable": ["carrot", "onion", "spinach", "lettuce", "potato", "broccoli", "tomato", "pepper", "cucumber"]
    }

    for category, keywords in categories.items():
        if word in keywords:
            return category

    return "unknown"


# Main Game Class
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

    def classify_and_confirm_words(self):
        self.new_words = [e.get().strip() for e in self.entries if e.get().strip()]
        if len(self.new_words) != 5:
            messagebox.showerror("Error", "Please enter exactly 5 words.")
            return

        self.classified_new_words = {word: classify_word(word) for word in self.new_words}
        # Remove unknown words
        # Remove unknown words
        self.new_words = [word for word in self.new_words if self.classified_new_words[word] != "unknown"]
        self.classified_new_words = {word: cat for word, cat in self.classified_new_words.items() if cat != "unknown"}

        if not self.new_words:
            messagebox.showerror("Error", "All entered words are unrecognized by the AI. Try different ones.")
            return


        result_window = tk.Toplevel(self.root)
        result_window.title("Classification Results")
        for word, cat in self.classified_new_words.items():
            tk.Label(result_window, text=f"{word} → {cat.title()}").pack()
        tk.Button(result_window, text="Start Game", command=lambda: [result_window.destroy(), self.start_game()]).pack()

    def start_game(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Filter out unknown DB words
        db_words = random.sample(word_database["automobile"] + word_database["animal"] + word_database["vegetable"], 5)
        self.game_words = db_words + self.new_words
        self.game_words = [word for word in self.game_words if classify_word(word) != "unknown"]

        random.shuffle(self.game_words)
        self.current_word_index = 0
        self.create_game_ui()
        self.root.bind("<Key>", self.handle_keypress)
        threading.Thread(target=self.play_next_word).start()

    def create_game_ui(self):
        self.status_label = tk.Label(self.root, text="Get Ready!", font=("Arial", 14, "bold"))
        self.status_label.pack()

        self.word_label = tk.Label(self.root, text="", font=("Arial", 24))
        self.word_label.pack(pady=10)

        frame = tk.Frame(self.root)
        frame.pack(pady=5)

        user_frame = tk.LabelFrame(frame, text="You", padx=10, pady=5)
        user_frame.grid(row=0, column=0, padx=20)
        self.user_labels = {}
        for i, cat in enumerate(["automobile", "animal", "vegetable"]):
            tk.Label(user_frame, text=cat.title()).grid(row=0, column=i)
            lbl = tk.Listbox(user_frame, height=10, width=15)
            lbl.grid(row=1, column=i)
            self.user_labels[cat] = lbl

        ai_frame = tk.LabelFrame(frame, text="AI Bot", padx=10, pady=5)
        ai_frame.grid(row=0, column=1, padx=20)
        self.ai_labels = {}
        for i, cat in enumerate(["automobile", "animal", "vegetable"]):
            tk.Label(ai_frame, text=cat.title()).grid(row=0, column=i)
            lbl = tk.Listbox(ai_frame, height=10, width=15)
            lbl.grid(row=1, column=i)
            self.ai_labels[cat] = lbl

        tk.Label(self.root, text="Controls: 1 = Automobile | 2 = Animal | 3 = Vegetable").pack(pady=5)

    def play_next_word(self):
        while self.current_word_index < len(self.game_words):
            self.current_word = self.game_words[self.current_word_index]
            self.word_label.config(text=self.current_word)

            ai_guess = classify_word(self.current_word)
            if ai_guess in self.ai_stacks:
                self.ai_stacks[ai_guess].append(self.current_word)
                self.ai_labels[ai_guess].insert(tk.END, self.current_word)
            else:
                print(f"AI skipped unknown word: {self.current_word}")
                self.current_word_index += 1
                continue

            correct_cat = self.get_correct_category(self.current_word)
            self.ai_results[self.current_word] = (ai_guess == correct_cat)

            time.sleep(2.5)
            self.current_word_index += 1
            if self.current_word_index >= len(self.game_words):
                break
            self.word_label.config(text=self.game_words[self.current_word_index])

        self.end_game()

    def get_correct_category(self, word):
        for category, words in word_database.items():
            if word in words:
                return category
        return self.classified_new_words.get(word, "unknown")

    def handle_keypress(self, event):
        key_map = {"1": "automobile", "2": "animal", "3": "vegetable"}
        if event.char in key_map and self.current_word_index < len(self.game_words):
            cat = key_map[event.char]
            word = self.current_word
            self.user_stacks[cat].append(word)
            self.user_labels[cat].insert(tk.END, word)
            correct_cat = self.get_correct_category(word)
            self.user_results[word] = (cat == correct_cat)

    def end_game(self):
        self.root.unbind("<Key>")
        correct_user = sum(self.user_results.values())
        correct_ai = sum(self.ai_results.values())
        result_text = f"{'AI Wins!' if correct_ai > correct_user else 'You Win!' if correct_user > correct_ai else 'Draw!'} (You: {correct_user}, AI: {correct_ai})"
        self.status_label.config(text=result_text)

        for cat, lst in self.user_labels.items():
            for i in range(lst.size()):
                word = lst.get(i)
                lst.itemconfig(i, {'fg': 'green' if self.user_results.get(word, False) else 'red'})

        for cat, lst in self.ai_labels.items():
            for i in range(lst.size()):
                word = lst.get(i)
                lst.itemconfig(i, {'fg': 'green' if self.ai_results.get(word, False) else 'red'})

        self.word_label.config(text="Game Over!")

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = ReflexGame(root)
    root.mainloop()
