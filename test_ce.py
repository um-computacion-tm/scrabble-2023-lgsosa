import unittest
from game_cell import Cell

class TestCell(unittest.TestCase):
    def test_init(self):
        cell = Cell (multiplier=2, multiplier_type="letter")

        #multiplier
        #multiplier.type

        self.assertEqual(
            cell.mutiplier,
            2,
        )
        self.assertEqual(
            cell.mutiplier_type,
            "letter",
        )