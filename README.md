# Tic-Tac-Toe AI

A Python implementation of the classic Tic-Tac-Toe game with an unbeatable AI opponent. The AI uses the **minimax algorithm** to search every possible game state and always plays the optimal move.

Built as a two-person project, including setting up a shared Git workflow from scratch.

## Features

- Human vs AI gameplay in a graphical pygame window
- AI plays optimally using minimax, so it never loses
- Click a square to place your mark
- Win, loss and draw detection with an on-screen message
- Press **R** to restart at any time

## Tech Stack

- Python 3
- pygame (graphics and input)
- NumPy (board representation)

## Running the Game

```bash
pip install pygame numpy
python tic-tac-toe.py
```

## How the AI Works

On its turn, the AI tries every empty square, then recursively plays out the rest of the game assuming both sides play perfectly. Each finished game is scored (AI win, loss or draw), and the AI picks the move with the best guaranteed outcome.
