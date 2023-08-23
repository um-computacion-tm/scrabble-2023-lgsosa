import unittest
from game_board import Board

class TestBoard(unittest.TestCase):
    def test_init (self):
        board = Board()
        self.assertEqual (
            len (board.grid),
            15
        )


if __name__ == "_main_":
    unittest.main()