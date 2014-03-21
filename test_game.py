import unittest
from board import GameBoard
from players import Player

class TestGameBoard(unittest.TestCase):
    def test_board_creation(self):
        game_board = GameBoard()
        self.assertIsInstance(game_board,GameBoard)

    def test_is_empty(self):
        game_board = GameBoard()
        self.assertTrue(game_board.is_cell_empty(1))

    def test_set_cell(self):
        game_board = GameBoard()
        game_board.set_cell(3,1)
        self.assertFalse(game_board.is_cell_empty(3))

class TestPlayer(unittest.TestCase):
    def test_player_creation(self):
        player = Player("Randy")
        name = player.name
        self.assertEqual(name,"Randy")



