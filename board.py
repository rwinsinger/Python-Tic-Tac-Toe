"""
  Class for tic tac toe game board
  Used to create the board, display it, check cells and set them
"""
class GameBoard:
    board = []              # Array to hold the board cells values 
    rowcols = 3             # Set the # of rows and cols (square)
    markers = {0: " "}      # Dictionary for cell value to marker 
   
    """ Build empty board when object is created """
    def __init__(self):
        self.reset()

    """ Give visual representation of board with players moves """
    def __str__(self):
        h_char = '-'
        v_char = '|'

        display = " "
        for x in range(self.rowcols):
            display += "   " + str(x + 1)
        display += "\n"

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

board = GameBoard()
print board
