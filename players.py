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
      Prompt for player name. Loops until something is entered and then returns 
      the name
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
      Handle a player's move. Will prompt for row, col of cell, validate, 
      verify cell is available and set cell or return error message
    """
    def make_move(self):
        not_valid = True

        while not_valid:
            player_move = raw_input("%s's Move (row,col): " % self.name)

            if self.coord_match.match(player_move):
                (row, col) = player_move.split(",", 2)

                # Get cell location base on row, col
                cell_offset = self.game_board.get_cell_offset(int(row),int(col))
                if (cell_offset >= 1):
                    # If empty, set the cell
                    if (self.game_board.is_cell_empty(cell_offset)):
                        self.game_board.set_cell(cell_offset, self.marker_value)
                        not_valid = False
                    else:
                        print "That spot is already taken, please try again..."
                else:
                    print "Rows and columns must be between 1 and 3"
            else:
                print "Please enter valid row number, a comma, and column number"


"""
  Computer player class - used for the computer player. 
"""
class ComputerPlayer(Player):
    # Same list as board win list, but in different order to aid in picking
    # next move.  Looks at possible wins with corners before middle ones
    poss_wins_adjusted = [[1,2,3],[7,8,9],[1,4,7],[3,6,9],
                          [1,5,9],[3,5,7],[4,5,6],[2,5,8]]
    check_cell_order = [5, 1, 3, 7, 9, 2, 4, 6, 8]
    first_move = True

    """
      Goes through the list, first checking to see in list what cells are
      empty - checks first, then last, then middle
      @params  array   - list of cells to be evaluated
      @returns integer - location of empty cell
    """
    def get_best_empty_cell(self, cell_list):
        for cell in [0,2,1]:
            if (self.game_board.is_cell_empty(cell_list[cell])):
                return (cell_list[cell])

    """
      Handle a computer player's move. Will determine the move based on state 
      of game board.  It will check to see if there is an opportunity to win 
      or a need to block.  If not, will play strategic locations first.
    """
    def make_move(self):
        made_move = False

        # If not the first move, loop through possible win combinations
        # and try to first find a combo that is one play away from win.
        if not self.first_move:
            to_win = []
            to_block = []
            to_play = []
            for win_combo in self.poss_wins_adjusted:
                total = self.game_board.sum_cells(win_combo)
                
                # Check for win - will add to win list and break
                # Checks for needed block - will add list to block list
                # Checks for area that is empty except for one of
                #   its own markers - will add to the play list
                if total == 8:
                    to_win.append(win_combo)
                    break
                elif total == 2:
                    to_block.append(win_combo)
                elif total == 4:
                    to_play.append(win_combo)

            if len(to_win):
                # If there is a possible win - play in empty cell
                cell_list = to_win.pop(0)

                # Get the empty cell
                cell = self.game_board.get_empty_cell(win_combo)

                # Play on that cell for win
                self.game_board.set_cell(cell, self.marker_value)
                made_move = True
            elif len(to_block):
                # If there is a need to block - play in empty cell
                cell_list = to_block.pop(0)

                # Get the empty cell
                cell = self.game_board.get_empty_cell(cell_list)

                # Play on that cell for block
                self.game_board.set_cell(cell, self.marker_value)
                made_move = True
            elif len(to_play):
                # If there is one already with computer's marker value
                # then play in best empty cell (first or last)
                cell_list = to_play.pop(0)

                # Get the best empty cell
                cell = self.get_best_empty_cell(cell_list)

                # Play on that cell for block
                self.game_board.set_cell(cell, self.marker_value)
                made_move = True

        # If first move or not part of combos
        if not made_move:
            # Loop through cells in specific order - play if cell is empty
            # Order is middle cell, corners, then other cells
            for cell in self.check_cell_order:
                # if cell is empty, set it
                if self.game_board.is_cell_empty(cell):
                    # Play on that cell                    
                    self.game_board.set_cell(cell, self.marker_value)
                    self.first_move = False
                    break
