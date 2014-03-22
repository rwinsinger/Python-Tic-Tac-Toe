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

print "\nWelcome to the TIC-TAC-TOE game!\n"

# Hard code this for now - will prompt later
num_players = 2

player_cnt = 0
# Prompt for player's names and then create player
while player_cnt < num_players:
    # Use static method to get name
    name = Player.get_player_name()

    # Create player and add to player list
    players.append(Player(name))
    player_cnt += 1

playing_game = True
while playing_game:
    print board

    moves = 0
    current_player_id = 0
    active_turn = True
    while active_turn:
        moves += 1
        # Grab the current player (based on id)
        player = players[current_player_id]
        
        print "%s's turn: Move #%d...\n" % (player.get_name(), moves)
        
        player.make_move()

        print board

        if (moves == 9):
           active_turn = False
        else:
            if (current_player_id == 1):
                current_player_id = 0
            else:
                current_player_id = 1
   
    playing_game = False

