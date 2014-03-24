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
    marker_values = [1,4]
    poss_wins = [[1,2,3],[4,5,6],[7,8,9],
                 [1,4,7],[2,5,8],[3,6,9],
                 [1,5,9],[3,5,7]]
    winner = False
   
    """ Build empty board when object is created """
    def __init__(self):
        self.reset()

    """
      Checks to see if cell is empty
      @returns boolean - true if value is 0, false if not 0
    """
    def is_cell_empty(self, loc):
        return (self.board[loc-1] == 0)

    """
      Sets a cell's value
    """
    def set_cell(self, loc, val):
        self.board[loc-1] = val

    """
      Get a cell's value
    """
    def get_cell(self, loc):
        return (self.board[loc-1])

    """
      Get a cell offset based off of row, col location
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
    """
    def sum_cells(self, cell_list):
        total = 0
        for cell in cell_list:
            total += self.get_cell(cell)
        return total

    """
      Get the first cell in passed list that is empty 
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
    """
    def get_marker_value_by_id(self, id):
        return(self.marker_values[id])

    """
      Checks for a winning line by looping through each possible winning combination and 
      summing up the values of the cells.  If value is 3, then first player is winner.
      If value is 12, then second player is the winner.
    """
    def check_for_win(self):
        game_won = False
        for win_combo in self.poss_wins:
            cells_total = self.sum_cells(win_combo)
            print "Win check: ",win_combo, cells_total
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

