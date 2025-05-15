# Reflex Stack - AI-Based Word Categorization Game

![Reflex Stack Logo](https://via.placeholder.com/150)

## 🎮 Overview

Reflex Stack is an interactive AI-based reflex game that challenges players to categorize words faster than an artificially intelligent opponent. The game tests your reflexes and knowledge by requiring quick categorization of words into three containers: Automobile, Animal, and Vegetable.

This project showcases the implementation of an autonomous rational AI agent with real-time learning capabilities, making each gameplay session unique and progressively challenging.

## ✨ Features

- **Competitive Gameplay**: Test your categorization speed against an AI opponent
- **Three Word Categories**: Automobile, Animal, and Vegetable
- **Dynamic Challenge**: Container order randomizes each round
- **AI Learning**: The AI improves over time using semantic similarity and WordNet ontology
- **Custom Words**: Add new words during gameplay to challenge the AI's learning capabilities
- **Performance Tracking**: Monitor your reaction times and scores

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/reflex-stack.git

# Navigate to the project directory
cd reflex-stack

# Install dependencies
pip install -r requirements.txt

# Run the game
python main.py


🎯 How to Play

Start the Game: Launch the application to begin
Controls: Use keys 1, 2, and 3 to select the appropriate container
Gameplay:

Words appear on screen one at a time
Press the corresponding key to categorize each word
Race against the AI to categorize correctly
First to correctly categorize all words wins



🧠 AI Implementation
Reflex Stack employs a sophisticated WordNet-based semantic similarity algorithm to classify words:

Pre-trained Classification: Common words are categorized using a trained model
Semantic Similarity: New words are classified based on their semantic distance to anchor words
Adaptive Learning: The system improves its classification accuracy over multiple gameplay sessions
WordNet Integration: Leverages the WordNet lexical database to understand word relationships

📊 Technical Architecture
Entity Relationship Diagram
The game utilizes a structured database design with the following entities:

Player: Stores user information and high scores
Game: Tracks individual gameplay sessions
Category: Manages the three classification categories
Word: Contains the dictionary of categorizable words
GameRound: Records data for each round played
RoundDetails: Stores detailed performance metrics

Classification Technique
The AI employs a three-step classification process:

WordNet Synsets retrieval
Path Similarity Score calculation
Average Similarity Computation across categories

👥 Contributors

Ali Zafar (@alizafar)
Shumail Ali (@shumailali)

🔮 Future Enhancements

Additional word categories
Difficulty levels
Multiplayer mode
Mobile application
Enhanced AI visualization

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
🙏 Acknowledgements

Department of Computer Science
Instructor: Faryal Farooq
WordNet lexical database