import re

"""
  Base player class - used for human player. 
"""
class Player:
    name = ""                           # Name of the player
    marker_value = 0                    # Marker value
    game_board = False                  # Will hold pointer to game board object
    coord_match = re.compile('\d,\d')   # Regex for correct coords entry

    """ Constructor to initialize player """
    def __init__(self, player_name, board, player_num):
        self.name = player_name
        self.game_board = board
        self.marker_value = board.get_marker_value_by_id(player_num)

    """ 
      Getter for player name
      @returns string - name of player
    """
    def get_name(self):
        return self.name

    """
      Prompt for player name. Loops until something is entered and then returns the name
      @returns string - name entered 
    """
    @staticmethod
    def get_player_name():
        valid = False
        while not valid:
            name = raw_input("Name of player: ")

            if len(name) > 0:
                valid = True

        return name

    """
      Handle a player's move. Will prompt for row, col of cell, validate, verify cell is available
      and set cell or return error message
    """
    def make_move(self):
        not_valid = True

        while not_valid:
            player_move = raw_input("%s's Move (row,col): " % self.name)

            if self.coord_match.match(player_move):
                (row, col) = player_move.split(",", 2)
                print "Player's move is: ", row, col

                cell_offset = self.game_board.get_cell_offset(int(row),int(col))
                if (cell_offset >= 0):
                    if (self.game_board.is_cell_empty(cell_offset)):
                        self.game_board.set_cell(cell_offset, self.marker_value)
                        not_valid = False
                    else:
                        print "That spot is already taken, please try again..."
                else:
                    print "Rows and columns must be between 1 and 3"
            else:
                print "Please enter valid row number, a comma, and column number"

