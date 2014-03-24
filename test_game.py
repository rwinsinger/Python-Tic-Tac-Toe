import unittest
from board import GameBoard
from players import Player, ComputerPlayer

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
        self.assertEquals(game_board.get_cell_offset(1,1), 1)
        self.assertEquals(game_board.get_cell_offset(3,3), 9)
        self.assertEquals(game_board.get_cell_offset(4,4), -1)
  
    """ Various tests to verify get marker by id method is working """
    def test_marker_valuet(self):
        game_board = GameBoard()
        self.assertEquals(game_board.get_marker_value_by_id(1),4)

    """ Test to verify sum of list of cells is correct """
    def test_cell_sum(self):
        game_board = GameBoard()
        game_board.set_cell(1,1)
        game_board.set_cell(2,3)
        game_board.set_cell(3,5)
        cell_list = [1,2,3]
        self.assertEquals(game_board.sum_cells(cell_list), 9)

    """ 
        Test to verify check_for_win. Try when board empty, then when has 
        winning combo 
    """
    def test_cell_sum(self):
        game_board = GameBoard()
        self.assertFalse(game_board.check_for_win())
        game_board.set_cell(3,1)
        game_board.set_cell(5,1)
        game_board.set_cell(7,1)
        self.assertTrue(game_board.check_for_win())

    """
        Test method that finds empty cell in list of cells
    """
    def test_find_empty_cell(self):
        game_board = GameBoard()
        game_board.set_cell(1,1)
        game_board.set_cell(2,1)
        cell_list = [1,2,3]
        cell = game_board.get_empty_cell(cell_list)
        print game_board
        self.assertTrue(cell,3)


class TestPlayer(unittest.TestCase):
    """ 
        Test player creation, is instance of Player object, and board is 
        instance of GameBoard 
    """
    def test_player(self):
        game_board = GameBoard()
        player = Player("Randy",game_board,0)
        name = player.name

        # Test name was set
        self.assertEqual(name,"Randy")
        # Test board is instance of GameBoard
        self.assertIsInstance(player.game_board,GameBoard)
        # Test player (id of 0) has marker value of 1
        self.assertEquals(player.marker_value, 1)

class TestComputerPlayer(unittest.TestCase):
    """ 
        Test computer player creation, is instance of ComputerPlayer object, 
        and board is instance of GameBoard 
    """
    def test_computer_player(self):
        game_board = GameBoard()
        computerplayer = ComputerPlayer("Computer",game_board,1)
        name = computerplayer.name

        # Test name was set
        self.assertEqual(name,"Computer")

        # Test board is instance of GameBoard
        self.assertIsInstance(computerplayer.game_board,GameBoard)
        # Test player (id of 1) has marker value of 4
        self.assertEquals(computerplayer.marker_value, 4)
        # Make the first move
        computerplayer.make_move()
        self.assertFalse(game_board.is_cell_empty(5))
        # Make the another move
        computerplayer.make_move()
        self.assertFalse(game_board.is_cell_empty(1))
        # Make the third move
        computerplayer.make_move()
        self.assertFalse(game_board.is_cell_empty(9))
        self.assertTrue(game_board.check_for_win())

