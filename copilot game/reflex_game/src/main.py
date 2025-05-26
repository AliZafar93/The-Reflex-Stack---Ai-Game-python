
import time
from game_logic.containers import Container
from game_logic.word_manager import WordManager
from game_logic.ai_bot import AIBot
from ui.display import display_word, display_containers, display_results
from utils.timer import Timer

def main():
    # Initialize game components
    containers = Container()
    word_manager = WordManager(containers)
    ai_bot = AIBot(containers)
    
    # Game setup
    rounds = 1
    total_rounds = 1  # You can change this for more rounds
    while rounds <= total_rounds:
        print(f"Round {rounds}!")
        
        # Start timer
        timer = Timer()
        timer.start()
        
        # Get words for this round
        words = word_manager.get_words_for_round()
        
        # Display words and containers
        for word in words:
            display_word(word)
            display_containers(containers)
            
            # Get user input
            user_input = input("Press 1 for Automobile, 2 for Animal, 3 for Vegetable: ")
            containers.add_word(word, user_input)
            
            # AI categorizes the word
            ai_bot.categorize_word(word)
        
        # Stop timer
        timer.stop()
        
        # Display results
        display_results(containers, timer)
        
        rounds += 1

if __name__ == "__main__":
    main()