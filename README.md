# Hangman Game using NLTK words

This is a Python Hangman game that uses words from the Natural Language Toolkit (NLTK) library. The player is given opportunities to guess the letters that make up a randomly selected word from the NLTK library. The player is given a set number of lives to guess the word correctly, and the game ends when the player has used up all their lives or they have guessed the word.

## Installation and Import of NLTK

- To use this code, you will need to install the NLTK library. You can do this using pip by running the command below in your terminal:

### Code
```pip install nltk```

- To import the library in your Python code, you can use the command `import nltk`.

## How to Play

The player is presented with a word, and their goal is to guess the letters that make up the word before they run out of lives. Each time the player guesses a letter, the game displays the current word with any correctly guessed letters filled in and any unknown letters replaced with a hyphen (-).

The player can only guess each letter once, and the game will keep track of all the letters that the player has already guessed. If the player guesses a letter that is not in the word, they lose a life. The game ends when the player has correctly guessed all the letters in the word, or they have run out of lives.

After each round, the player is given the option to play again or quit the game.
