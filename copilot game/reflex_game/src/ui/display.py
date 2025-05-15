from time import sleep

def display_welcome_message():
    print("Welcome to the Reflex Game!")
    print("You will categorize words into three containers:")
    print("1. Automobile")
    print("2. Animal")
    print("3. Vegetable")
    print("Press the corresponding number to categorize the word displayed.")
    print("Let's see how fast you can react!\n")

def display_word(word):
    print(f"Word: {word}")

def display_containers():
    print("Containers:")
    print("1. Automobile")
    print("2. Animal")
    print("3. Vegetable")

def display_game_status(player_time, ai_time):
    print(f"Your time: {player_time:.2f} seconds")
    print(f"AI time: {ai_time:.2f} seconds")
    if player_time < ai_time:
        print("You win!")
    elif player_time > ai_time:
        print("AI wins!")
    else:
        print("It's a tie!")

def display_new_word_prompt():
    print("A new word has been added! Please categorize it.")