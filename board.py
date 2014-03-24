"""
  Class for tic tac toe game board
  Used to create the board, display it, check cells and set them
"""
class GameBoard:
    board = []              # Array to hold the board cells values 
    rowcols = 3             # Set the # of rows and cols (square)
    markers = {             # Dictionary for cell value to marker 
        0: " ",
        1: "O",
        4: "X"
        }
    marker_values = [1,4]   # Values to use for the two players
                            # List of winning cell combinations
    poss_wins = [[1,2,3],[4,5,6],[7,8,9],
                 [1,4,7],[2,5,8],[3,6,9],
                 [1,5,9],[3,5,7]]
    winner = False          # Will hold player that wins
   
    """ Build empty board when object is created """
    def __init__(self):
        self.reset()

    """
      Checks to see if cell is empty
      @params  integer - location of cell to check
      @returns boolean - true if value is 0, false if not 0
    """
    def is_cell_empty(self, loc):
        return (self.board[loc-1] == 0)

    """
      Sets a cell's value
      @params  integer - location of cell to set
               integer - value to set
    """
    def set_cell(self, loc, val):
        self.board[loc-1] = val

    """
      Get a cell's value
      @params  integer - location of cell to get
      @returns integer - value retrieved from cell
    """
    def get_cell(self, loc):
        return (self.board[loc-1])

    """
      Get a cell offset based off of row, col location
      @params  integer - row of board
               integer - column of board
      @returns integer - location of cell 
    """
    def get_cell_offset(self, row, col):
        offset = -1
        if (row in range(1,4) and col in range(1,4)):
            offset = (3 *(row - 1)) + (col)

        return (offset)

    """
      Add up total of values in the cells.  This will be used to 
      determine if a win has happened, but also to determine what plays
      have been made
      @params  array   - list of cells
      @returns integer - sum of the values of cells in the list
    """
    def sum_cells(self, cell_list):
        total = 0
        for cell in cell_list:
            total += self.get_cell(cell)
        return total

    """
      Get the first cell in passed list that is empty 
      @params  array   - list of cells
      @returns integer - location of cell in array (1-9)
    """
    def get_empty_cell(self, cell_list):
        # Loop through each cell on thelist
        for cell in cell_list:
            if self.is_cell_empty(cell):
                break
        return cell

    """
      Get the marker value for the given id
      @params  integer - player id (0 or 1)
      @returns integer - value for that player
    """
    def get_marker_value_by_id(self, id):
        return(self.marker_values[id])

    """
      Checks for a winning line by looping through each possible winning 
      combination and summing up the values of the cells.  If value is 3, 
      then first player is winner.  If value is 12, then second player 
      is the winner.
      @returns boolean - True if game one, false if not
    """
    def check_for_win(self):
        game_won = False
        for win_combo in self.poss_wins:
            cells_total = self.sum_cells(win_combo)

            # if totals are sum of first player or second player values
            # then we have a win.
            if (cells_total == 3) or (cells_total == 12):
                game_won = True
                break

        return game_won

    """ 
      Give visual representation of board with players moves 
      @returns string - string representation of board's current state
    """
    def __str__(self):
        h_char = '-'
        v_char = '|'

        # Print top numbers
        display = " "
        for x in range(self.rowcols):
            display += "   " + str(x + 1)
        display += "\n"

        # Loop through rows and columns, building board and showing
        # cell values (if any)
        cell = 1
        for row in range(self.rowcols):
            display += "  " + h_char*13 + "\n"
            display += str(row + 1) +" | " 
            for col in range(self.rowcols):
                display += self.markers[self.get_cell(cell)] + " | "
                cell += 1

            display += "\n"

        display += "  " + h_char*13 + "\n"

        return display 

    """ Resets the board so that all cells are 0 (shown as blank) """
    def reset(self):
        self.board = [0 for i in xrange(self.rowcols * self.rowcols)]

