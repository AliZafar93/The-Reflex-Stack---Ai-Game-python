# Reflex-Based Game

## Overview
The Reflex-Based Game is a fun and interactive game designed to test players' reflexes by categorizing words into three containers: Automobile, Animal, and Vegetable. Players compete against an AI bot that learns and adapts to new words added during gameplay.

## Features
- Three categories for word classification: Automobile, Animal, and Vegetable.
- A competitive AI bot that plays alongside the user.
- Dynamic word management that allows users to add new words during gameplay.
- Real-time tracking of players' reflex times.

## Project Structure
```
reflex_game
├── src
│   ├── main.py                # Entry point of the game
│   ├── game_logic
│   │   ├── __init__.py
│   │   ├── containers.py       # Defines the Container class for word categories
│   │   ├── word_manager.py      # Manages word selection and addition
│   │   └── ai_bot.py           # Simulates the AI player
│   ├── ui
│   │   ├── __init__.py
│   │   └── display.py          # Handles the user interface
│   └── utils
│       ├── __init__.py
│       └── timer.py            # Provides timing functionality
├── tests
│   ├── test_containers.py      # Unit tests for the Container class
│   ├── test_word_manager.py     # Unit tests for the WordManager class
│   ├── test_ai_bot.py          # Unit tests for the AIBot class
│   └── test_timer.py           # Unit tests for the Timer class
├── requirements.txt            # Lists project dependencies
└── README.md                   # Project documentation
```

## Setup Instructions
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using:
   ```
   pip install -r requirements.txt
   ```
4. Run the game by executing:
   ```
   python src/main.py
   ```

## Gameplay
- Players will see a word displayed on the screen.
- They must categorize the word by pressing the corresponding key (1 for Automobile, 2 for Animal, 3 for Vegetable).
- The AI bot will also categorize the same words, and the player who finishes first wins the round.
- Players can add new words during the game, which the AI will learn to categorize correctly.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.