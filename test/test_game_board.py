import unittest
from game.game_board import Board
from game.models import Tile

class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(
            len(board.grid),
            15,
        )
        self.assertEqual(
            len(board.grid[0]),
            15,
        )
        self.assertEqual(
            len(board.grid[0]),
            15,
        )

    def test_board_cell_00(self):
        board = Board()
        cell = board.grid
        self.assertEqual(cell[0][0].multiplier,3 )
        self.assertEqual(cell[0][0].multiplier_type,'word' )
    
    def test_board_cell_77(self):
        board = Board()
        cell = board.grid
        self.assertEqual(cell[7][7].multiplier,2 )
        self.assertEqual(cell[7][7].multiplier_type,'word' )

    def test_place_tile(self):
        board = Board()
        tile = Tile('A', 1)
        self.assertTrue(board.place_tile(7, 7, tile))
        self.assertFalse(board.place_tile(7, 7, tile))


if __name__ == '__main__':
    unittest.main()