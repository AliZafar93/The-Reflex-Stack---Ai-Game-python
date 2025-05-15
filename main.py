import tkinter as tk
import random

# -------------------
# Word Setup
# -------------------
CATEGORIES = ['Automobile', 'Animal', 'Vegetable']
CATEGORY_KEYS = {'1': 'Automobile', '2': 'Animal', '3': 'Vegetable'}
WORD_DATABASE = {
    'Automobile': ['car', 'truck', 'ferrari'],
    'Animal': ['cat', 'dog', 'lion'],
    'Vegetable': ['carrot', 'onion', 'spinach']
}
UNKNOWN_WORDS = ['falcon', 'jeep', 'broccoli']
ALL_WORDS = list({word for words in WORD_DATABASE.values() for word in words}) + UNKNOWN_WORDS
random.shuffle(ALL_WORDS)

# Simple reflex AI agent
def ai_predict(word):
    for category, words in WORD_DATABASE.items():
        if word in words:
            return category
    return random.choice(CATEGORIES)

# -------------------
# GUI Game Class
# -------------------
class ReflexGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Reflex Game: Independent AI")

        self.current_word_index = 0
        self.current_word = ALL_WORDS[self.current_word_index]

        self.user_stacks = {cat: [] for cat in CATEGORIES}
        self.ai_stacks = {cat: [] for cat in CATEGORIES}
        self.correct_user = 0
        self.correct_ai = 0

        self.setup_ui()
        self.display_word()

        self.root.bind("<Key>", self.key_pressed)

    def setup_ui(self):
        # Controls
        control_text = "Controls: 1 = Automobile | 2 = Animal | 3 = Vegetable"
        tk.Label(self.root, text=control_text, font=("Helvetica", 12)).pack()

        # Current Word
        self.word_label = tk.Label(self.root, text="", font=("Helvetica", 24), pady=20)
        self.word_label.pack()

        # Horizontal layout
        self.game_frame = tk.Frame(self.root)
        self.game_frame.pack()

        self.user_box = self.create_player_box(self.game_frame, "You", self.user_stacks)
        self.ai_box = self.create_player_box(self.game_frame, "AI Bot", self.ai_stacks)

        # Result
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 16, "bold"), fg="green")
        self.result_label.pack(pady=10)

    def create_player_box(self, parent, title, stacks_dict):
        frame = tk.Frame(parent, bd=2, relief=tk.SUNKEN, padx=10, pady=10)
        frame.pack(side=tk.LEFT, padx=30)

        tk.Label(frame, text=title, font=("Helvetica", 14, 'bold')).pack()

        row = tk.Frame(frame)
        row.pack()

        stack_labels = {}
        for category in CATEGORIES:
            col = tk.Frame(row)
            col.pack(side=tk.LEFT, padx=5)
            tk.Label(col, text=category, font=("Helvetica", 10)).pack()
            label = tk.Label(col, text="", width=15, height=10, bg="white", relief=tk.GROOVE, justify=tk.LEFT, anchor="n")
            label.pack()
            stack_labels[category] = label
        return stack_labels

    def key_pressed(self, event):
        key = event.char
        if key not in CATEGORY_KEYS:
            return

        category = CATEGORY_KEYS[key]
        self.user_stacks[category].append(self.current_word)

        if self.current_word in WORD_DATABASE.get(category, []):
            self.correct_user += 1

        self.update_stack(self.user_box, self.user_stacks)

    def display_word(self):
        if self.current_word_index >= len(ALL_WORDS):
            self.end_game()
            return

        self.current_word = ALL_WORDS[self.current_word_index]
        self.word_label.config(text=f"Word: {self.current_word}")

        self.root.after(1000, self.ai_play)

    def ai_play(self):
        word = self.current_word
        category = ai_predict(word)
        self.ai_stacks[category].append(word)

        if word in WORD_DATABASE.get(category, []):
            self.correct_ai += 1

        self.update_stack(self.ai_box, self.ai_stacks)

        self.current_word_index += 1
        self.root.after(300, self.display_word)

    def update_stack(self, stack_box, stacks_data):
        for category, words in stacks_data.items():
            stack_box[category].config(text="\n".join(words))

    def end_game(self):
        self.word_label.config(text="Game Over!")
        if self.correct_user > self.correct_ai:
            result = f"You win! 🎉 (You: {self.correct_user} | AI: {self.correct_ai})"
        elif self.correct_user < self.correct_ai:
            result = f"AI wins! 🤖 (You: {self.correct_user} | AI: {self.correct_ai})"
        else:
            result = f"It's a tie! 😎 (You: {self.correct_user} | AI: {self.correct_ai})"
        self.result_label.config(text=result)

# -------------------
# Run GUI
# -------------------
if __name__ == "__main__":
    root = tk.Tk()
    game = ReflexGame(root)
    root.mainloop()
