from board import GameBoard
from players import Player

"""
  This is the main logic for the game.  It will:
    - create the board
    - prompt for number of players (human/computer)
    - prompt for player names
    - loop - allowing for multiple games for same players
    - loop - for each player move - re-displaying board each time
    - check for winner and display winner name or tie if game over
    - prompt to see if they want to play again
"""

# Create array to hold players
players = []

board = GameBoard()

print board
