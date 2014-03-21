"""
  Base player class - used for human player. 
"""
class Player:
    name = ""

    """ Constructor to initialize player """
    def __init__(self, player_name):
        self.name = player_name

    """ 
      Getter for player name
      @returns string - name of player
    """
    def get_name(self):
        return self.name
