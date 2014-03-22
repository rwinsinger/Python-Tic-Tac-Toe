import unittest
from board import GameBoard
from players import Player

class TestGameBoard(unittest.TestCase):
    """ Test game board creation and is instance of that object """
    def test_board_creation(self):
        game_board = GameBoard()
        self.assertIsInstance(game_board,GameBoard)

    """ Check that a cell is empty on new board """
    def test_is_empty(self):
        game_board = GameBoard()
        self.assertTrue(game_board.is_cell_empty(1))

    """ Set a cell, then make sure it isn't empty """
    def test_set_cell(self):
        game_board = GameBoard()
        game_board.set_cell(3,1)
        self.assertFalse(game_board.is_cell_empty(3))

    """ Set a cell, then make value in it matches what you set it """
    def test_get_cell(self):
        game_board = GameBoard()
        game_board.set_cell(3,1)
        self.assertEquals(game_board.get_cell(3), 1)

    """ Various tests to verify row,col conversion is working """
    def test_get_cell_offset(self):
        game_board = GameBoard()
        self.assertEquals(game_board.get_cell_offset(1,1), 0)
        self.assertEquals(game_board.get_cell_offset(3,3), 8)
        self.assertEquals(game_board.get_cell_offset(4,4), -1)
  
    """ Test to verify sum of list of cells is correct """
    def test_cell_sum(self):
        game_board = GameBoard()
        game_board.set_cell(1,1)
        game_board.set_cell(2,3)
        game_board.set_cell(3,5)
        list = [1,2,3]
        self.assertEquals(game_board.sum_cells(list), 9)

class TestPlayer(unittest.TestCase):
    """ Test player creation, is instance of Player object, and board is instance of GameBoard """
    def test_player_creation(self):
        game_board = GameBoard()
        player = Player("Randy",game_board)
        name = player.name
        self.assertEqual(name,"Randy")
        self.assertIsInstance(player.game_board,GameBoard)

