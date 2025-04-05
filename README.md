# Hangman Game

A classic Hangman game implemented in Python, where players guess letters to uncover a hidden word before running out of attempts.

## Description
This project is a Python implementation of the classic Hangman word-guessing game. Players attempt to guess a hidden word by suggesting letters one at a time. For each incorrect guess, part of a hangman figure is drawn. The game continues until the player either guesses the word correctly or the hangman figure is completed.

## Features
- Random word selection from a large vocabulary
- Visual hangman display that updates with each incorrect guess
- Input validation to handle invalid or repeated guesses
- Play-again option after each game
- Clear display of used letters and current word progress

## How It Works
The game follows these steps:
1. A random word is selected from the predefined word list
2. The player guesses letters one at a time
3. Correct guesses reveal the letter's position(s) in the word
4. Incorrect guesses reduce the remaining attempts and add to the hangman drawing
5. The game ends when either:
   - The player guesses all letters in the word (win)
   - The player runs out of attempts (lose)

## Workflow Overview

### Initialization:
- Select a random word and convert to uppercase
- Initialize sets for tracking used letters and word letters
- Set initial lives (6 attempts)

### Game Loop:
- Display current game state (used letters, word progress, hangman)
- Get player input and validate
- Update game state based on guess correctness
- Check win/lose conditions

### Termination:
- Display final result (win/lose message with the word)
- Offer to play again

## Code Structure
- `hangman.py`: Main game logic and flow
- `hangman_display.py`: ASCII art for hangman visualization
- `words.py`: Extensive word list for the game

## Running the Game
```bash
python hangman.py
