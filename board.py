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
        return (self.board[loc] == 0)

    """
      Sets a cell's value
    """
    def set_cell(self, loc, val):
        self.board[loc] = val

    """
      Get a cell's value
    """
    def get_cell(self, loc):
        return (self.board[loc])

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
        idx = 0
        for row in range(self.rowcols):
            display += "  " + h_char*13 + "\n"
            display += str(row + 1) +" | " 
            for col in range(self.rowcols):
                display += self.markers[self.board[idx]] + " | "
                idx += 1

            display += "\n"

        display += "  " + h_char*13 + "\n"

        return display 

    """ Resets the board so that all cells are 0 (shown as blank) """
    def reset(self):
        self.board = [0 for i in xrange(self.rowcols * self.rowcols)]

