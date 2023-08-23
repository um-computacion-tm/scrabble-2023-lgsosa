import unittest
from models import (
    BagTiles,
    Tile,
)
from unittest.mock import patch


class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)


class TestBagTiles(unittest.TestCase):
    @patch('random.shuffle')
    def test_bag_tiles(self, patch_shuffle):
        bag = BagTiles()
        self.assertEqual(
            len(bag.tiles),
            102,
        )
        self.assertEqual(
            patch_shuffle.call_count,
            1,
        )
        self.assertEqual(
            patch_shuffle.call_args[0][0],
            bag.tiles,
        )


    def test_take(self):
        bag = BagTiles()
        tiles = bag.take(2)
        self.assertEqual(
            len(bag.tiles),
            100,
        )
        self.assertEqual(
            len(tiles),
            2,
        )

    def test_put(self):
        bag = BagTiles()
        put_tiles = [Tile('Z', 1), Tile('Y', 1)]
        bag.put(put_tiles)
        self.assertEqual(
            len(bag.tiles),
            104,
        )
       
    def tomar_mas_fichas(self):
        bag = BagTiles()
        self.assertRaises(IndexError)(
            tiles = bag.take(200))
        
    def fichas_que_no_estan(self):
        bag = BagTiles()
        invalid_tiles = [Tile('A', 1), Tile('B', 2)]  # Fichas que no están en la bolsa
        self.assertRaises(ValueError)(
            bag.put(invalid_tiles))
    

if __name__ == '__main__':
    unittest.main()

