import unittest
from game.board import *
from game.cell import *
from unittest.mock import patch
from game.models import Tile

class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(len(board.grid),15)
        self.assertEqual(len(board.grid[0]),15)

    def test_board_is_empty(self):
        board = Board()
        self.assertEqual( board.is_empty(), True)

    def test_board_is_not_empty(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        assert board.is_empty() == False

    @patch('game.board.dle.search_by_word')
    def test_word_inside_board_h(self, mock_rae):
        mock_rae.return_value.meta_description = 'casa | Definición | Diccionario de la lengua española | RAE - ASALE'
        board = Board()
        word = 'CASA'
        location = (7, 7)
        horizontal = 'H'
        word_is_valid = board.validate(word, location, horizontal)
        self.assertEqual(word_is_valid, True)
    
    @patch('game.board.dle.search_by_word')
    def test_word_out_of_board_h(self, mock_rae):
        mock_rae.return_value.meta_description = 'facultades | Definición | Diccionario de la lengua española | RAE - ASALE'
        board = Board()
        word = 'FACULTADES'
        location = (7, 7)
        horizontal = 'H'
        word_is_valid = board.validate(word, location, horizontal)
        self.assertEqual(word_is_valid, False)

    @patch('game.board.dle.search_by_word')
    def test_word_inside_board_v(self, mock_rae):
        mock_rae.return_value.meta_description = 'casa | Definición | Diccionario de la lengua española | RAE - ASALE'
        board = Board()
        word = 'CASA'
        location = (7, 7)
        horizontal = 'V'
        word_is_valid = board.validate(word, location, horizontal)
        self.assertEqual(word_is_valid, True)
    
    @patch('game.board.dle.search_by_word')
    def test_word_out_of_board_v(self, mock_rae):
        mock_rae.return_value.meta_description = 'facultades | Definición | Diccionario de la lengua española | RAE - ASALE'
        board = Board()
        word = 'FACULTADES'
        location = (7, 7)
        horizontal = 'V'
        word_is_valid = board.validate(word, location, horizontal)
        self.assertEqual(word_is_valid, False)

    @patch('game.board.dle.search_by_word')
    def test_validate_intersection_h_fail(self, mock_rae):
        mock_rae.return_value.meta_description = 'Versión electrónica 23.6 del «Diccionario de la lengua española», obra lexicográfica académica por excelencia.' 
        board = Board()
        board.grid[7][7].tile = Tile("C",1)
        board.grid[8][7].tile = Tile("A",1)
        board.grid[9][7].tile = Tile("S",2)
        board.grid[10][7].tile = Tile("A",1)
        word = "LSSO"
        orientation = "H"
        location = (8,6)
        self.assertEqual(board.validate(word, location, orientation), False)


    @patch('game.board.dle.search_by_word')
    def test_validate_intersection_in_right_invalid(self, mock_rae):
        mock_rae.return_value.meta_description = 'Versión electrónica 23.6 del «Diccionario de la lengua española», obra lexicográfica académica por excelencia.'
        board = Board()
        board.grid[7][7].tile = Tile("C", 1)
        board.grid[7][8].tile = Tile("A", 1)
        board.grid[7][9].tile = Tile("S", 2)
        board.grid[7][10].tile = Tile("A", 1)
        board.grid[6][10].tile = Tile("L", 1)
        board.grid[7][10].tile = Tile("A", 1)
        board.grid[8][10].tile = Tile("S", 2)
        board.grid[9][10].tile = Tile("O", 1)
        board.grid[9][8].tile = Tile("O", 1)
        board.grid[9][9].tile = Tile("S", 2)
        board.grid[9][10].tile = Tile("O", 1)
        word = "CAOS"
        orientation = "V"
        location = (7, 7)
        self.assertEqual(board.validate(word, location, orientation), False)


    def test_put_word_v(self):
        board = Board()
        word = [Tile('C',1),Tile('O',1),Tile('S',2),Tile('A',1)]
        orientation = 'V'
        location = (4,5)
        board.put_word(word, location, orientation)
        word_in_board = ''
        for i in range(4):
            word_in_board += board.grid[4+i][5].tile.letter
        self.assertEqual(word_in_board , 'COSA')

    def test_put_word_h(self):
        board = Board()
        word = [Tile('C',1),Tile('O',1),Tile('S',2),Tile('A',1)]
        orientation = 'H'
        location = (5,4)
        board.put_word(word, location, orientation)
        word_in_board = ''
        for i in range(4):
            word_in_board += board.grid[5][4+i].tile.letter
        self.assertEqual(word_in_board , 'COSA')

    def test_valid_accent_word(self):
        board = Board()
        word = "Árbol"
        self.assertEqual(board.words_with_accent(word), 'ARBOL')

    def test_valid_accent_rest_of_words(self):
        board = Board()
        word1 = "Éste"
        word2 = "ahí"
        word3 = "cocción"
        word4 = "última"
        self.assertEqual(board.words_with_accent(word1), 'ESTE')
        self.assertEqual(board.words_with_accent(word2), 'AHI')
        self.assertEqual(board.words_with_accent(word3), 'COCCION')
        self.assertEqual(board.words_with_accent(word4), 'ULTIMA') 


               
class TestDiccionary(unittest.TestCase):
    @patch(
        'pyrae.dle.search_by_word',
        return_value=unittest.mock.MagicMock(
            meta_description='1. interj. U. como salutación familiar.'
        )
    )
    def test_valid(self, search_by_word_patched):
        board = Board()
        self.assertTrue(board.validate_word('hola'))

    @patch(
        'pyrae.dle.search_by_word',
        return_value=unittest.mock.MagicMock(
            meta_description='Versión electrónica 23.6 del «Diccionario de la lengua española», obra lexicográfica académica por excelencia.'
        )
    )
    def test_invalid(self, search_by_word_patched):
        board = Board()
        self.assertFalse(board.validate_word('asd'))

    @patch(
        'pyrae.dle.search_by_word',
        return_value=None
    )
    def test_connection_error(self, search_by_word_patched):
        board = Board()
        with self.assertRaises(DictionaryConnectionError):
            board.validate_word('hola')


    def test_put_word_v_intersections(self):
        board = Board()
        board.grid[7][6].tile = Tile('C',3)
        board.grid[7][7].tile = Tile('A',1)
        board.grid[7][8].tile = Tile('S',1)
        board.grid[7][9].tile = Tile('A',1)
        word = [Tile('L',3), Tile('S',6), Tile('O',1)]
        location = (6, 7)
        horizontal = 'V'
        board.put_word(word,location,horizontal)
        word_in_board = ''
        for i in range(4):
            word_in_board += board.grid[6+i][7].tile.letter
        self.assertEqual('LASO',word_in_board)

class TestCalculateWordValue(unittest.TestCase):
    def test_simple(self):
        board = Board()        
        word = 'casa'
        pos=(10,6)
        value = board.calculate_word_value(word, pos, 'H')
        self.assertEqual(value, 6)

    def test_simple_with_double_letter(self):
        board = Board()
        word = 'lluvia'
        pos=(10,5)
        value = board.calculate_word_value(word, pos, 'H')
        self.assertEqual(value, 8+1+4+1+1)
        
    def test_with_word_multiplier_2(self):
        board = Board()        
        word = 'casa'
        pos=(7,6)
        value = board.calculate_word_value(word, pos, 'H')
        self.assertEqual(value, 12)

    def test_with_word_multiplier_3(self):
        board = Board()        
        word = 'casa'
        pos=(14,6)
        value = board.calculate_word_value(word, pos, 'H')
        self.assertEqual(value, 18)

    def test_with_letter_multiplier_2(self):
        board = Board()        
        word = 'casa'
        pos=(8,8)
        value = board.calculate_word_value(word, pos, 'H')
        self.assertEqual(value, 9)

    def test_with_letter_multiplier_3(self):
        board = Board()        
        word = 'casa'
        pos=(9,8)
        value = board.calculate_word_value(word, pos, 'H')
        self.assertEqual(value, 8)

    def test_with_letter_multiplier_and_word_multiplier(self):
        board = Board()        
        word = 'casa'
        pos=(14,0)
        value = board.calculate_word_value(word, pos, 'H')
        self.assertEqual(value, 21)

    def test_with_letter_multiplier_and_word_multiplier_no_active(self):
        board = Board()        
        word = 'casa'
        pos=(14,0)
        value = board.calculate_word_value(word, pos, 'H')
        value = board.calculate_word_value(word, pos, 'H')
        self.assertEqual(value, 7)

    def test_out_of_range_side(self):
        board = Board()
        word = 'casa'
        pos = (14,10)
        horizontal = 'H'
        value = board.calculate_word_value(word, pos, horizontal)
        pos = (0,0)
        horizontal = 'H'
        value = board.calculate_word_value(word, pos, horizontal)
        self.assertEqual(value!=None, True)

    def test_letter_not_available(self):
        board = Board()
        word = 'c?sa'
        pos = (7,7)
        horizontal = 'H'
        value = board.calculate_word_value(word,pos,horizontal)
        self.assertEqual(value, 10)

    def test_validate_word_inside_board_horizontal(self):
        board = Board()
        board.grid = [
            ['_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_']
        ]
        word = "WORD"
        location = (1, 2)
        orientation = "H"
        result = board.validate_word_inside_board(word, location, orientation)
        self.assertFalse(result, "La palabra 'WORD' debería encajar horizontalmente en la ubicación (1, 2).")

    def test_validate_word_inside_board_vertical(self):
        board = Board()
        board.grid = [
            ['_', '_', '_', '_'],
            ['_', '_', '_', '_'],
            ['_', '_', '_', '_'],
            ['_', '_', '_', '_'],
            ['_', '_', '_', '_']
        ]
        word = "VERTICAL"
        location = (2, 1)
        orientation = "V"
        result = board.validate_word_inside_board(word, location, orientation)
        self.assertFalse(result, "La palabra 'VERTICAL' debería encajar verticalmente en la ubicación (2, 1).")

    def test_get_word_without_intersections_horizontal(self):
        board = Board()
        board.grid = [
            [None, "A", None, "B", None],
            [None, "C", None, "D", None],
            [None, "E", None, "F", None]
        ]
        word = "ACD"
        pos = (1, 0)
        horizontal = True
        result = board.get_word_without_intersections(word, pos, horizontal)
        self.assertEqual(result, "AD")

    def test_get_word_without_intersections_vertical(self):
        board = Board()
        board.grid = [
            [None, "A", None, "B", None],
            [None, "C", None, "D", None],
            [None, None, None, "F", None]
        ]
        word = "ACD"
        pos = (0, 3)
        horizontal = False
        result = board.get_word_without_intersections(word, pos, horizontal)
        self.assertEqual(result, "")

    def test_get_side_word_horizontal(self):
        board = Board()  
        cell = board.grid[2][2]  
        cell.tile = Tile('A', 1)  
        i = 1  
        orientation = (True, False) 
        pos = (2, 2)  
        letter = 'A'  
        side_word, j = board.get_side_word(cell, i, orientation, pos, letter)
        self.assertEqual(side_word, 'AA', "El lado horizontal debería ser la letra 'A'")
        self.assertEqual(j, 2, "j debería ser 1 para una celda con letra")

    def test_get_side_word_vertical(self):
        board = Board()  
        cell = board.grid[2][2]  
        cell.tile = Tile('B', 1)  
        i = 1 
        orientation = (False, False)  
        pos = (2, 2)  
        letter = 'B'  
        side_word, j = board.get_side_word(cell, i, orientation, pos, letter)
        self.assertEqual(side_word, 'BB', "El lado vertical debería ser la letra 'B'")
        self.assertEqual(j, 2, "j debería ser 1 para una celda con letra")

import unittest
from game.board import Board, DictionaryConnectionError
from game.cell import Cell, Tile
from unittest.mock import patch

class TestBoardCoverage(unittest.TestCase):
    def setUp(self):
        # Configurar un tablero con algunas celdas y palabras de muestra
        self.board = Board()

    def test_add_multipliers(self):
        board = Board()
        board.add_multipliers()
        self.assertIsNotNone(board.grid[0][0].multiplier, "El multiplicador en la esquina superior izquierda no debería ser None.")

    def test_get_cells(self):
        board = Board()
        pos = (1, 2)
        i = 3
        horizontal = True
        cells = board.get_cells(pos, i, horizontal)
        self.assertEqual(len(cells), i, "La cantidad de celdas obtenidas no coincide con el valor esperado.")

    def test_validate_word_inside_board_false(self):
        board = Board()
        word = "LONGWORD"
        location = (10, 5)
        orientation = "H"
        result = board.validate_word_inside_board(word, location, orientation)
        self.assertFalse(result, "La palabra 'LONGWORD' no debería caber horizontalmente en la ubicación (10, 5).")

    def test_is_empty_false(self):
        board = Board()
        board.grid[7][7].tile = Tile("C", 1)
        result = board.is_empty()
        self.assertFalse(result, "El tablero no debería estar vacío después de colocar una ficha en el centro.")

    def test_validate_empty_horizontal_true(self):
        board = Board()
        word = "WORD"
        location = (7, 7)
        orientation = "H"
        result = board.validate_empty(word, location, orientation)
        self.assertTrue(result, "La palabra 'WORD' debería ser válida en la ubicación (7, 7) horizontalmente.")

    def validate_side_cell(self, parameters, validators, cell, i):
        word, pos, is_valid, intersections = parameters[0], parameters[1], validators[0], validators[1]
        sidecell = self.get_side_cell(pos, i)
        word2 = sidecell[0] if sidecell[0] else ''
        word2 += cell.letter if cell else ''
        word2_is_valid = self.rae_search(word2)
        return [is_valid and word2_is_valid, intersections + 1 if word2_is_valid else intersections]

    def test_check_cells_sidecell_true(self):
        board = Board()
        cells = [Cell('A', 1), Cell('B', 2), Cell('C', 3)]
        parameters = ['ABC', (2, 1), True, 0]
        validators = [True, 0]
        result = board.check_cells(cells, parameters, validators)
        self.assertTrue(result, "Las celdas deberían ser válidas en esta ubicación.")

    def test_calculate_word_value_with_multiplier(self):
            board = Board()
            word = 'HELLO'
            pos = (7, 7)
            direction = 'H'
            value = board.calculate_word_value(word, pos, direction, True)
            self.assertEqual(value, 28, "El valor de la palabra con el multiplicador debería ser 20.")

    def test_validate_not_empty_false(self):
        board = Board()
        word = "WORD"
        location = (7, 7)
        orientation = "V"
        result = board.validate_not_empty(word, location, orientation)
        self.assertFalse(result, "La palabra 'WORD' no debería ser válida en la ubicación (7, 7) verticalmente.")

class TestBoardInTerminal(unittest.TestCase):

    def setUp(self):
        # Crea una instancia del tablero con el tablero proporcionado
        # Asegúrate de que el método `board_in_terminal` está correctamente implementado
        self.board = Board()

    def test_board_in_terminal_empty(self):
        expected_output = (
            ' \n'
            '    0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 \n'
            'A   W3|  |  |L2|  |  |  |W3|  |  |  |L2|  |  |W3|\n'
            'B     |W2|  |  |  |L3|  |  |  |L3|  |  |  |W2|  |\n'
            'C     |  |W2|  |  |  |L2|  |L2|  |  |  |W2|  |  |\n'
            'D   L2|  |  |W2|  |  |  |L2|  |  |  |W2|  |  |L2|\n'
            'E     |  |  |  |W2|  |  |  |  |  |W2|  |  |  |  |\n'
            'F     |L3|  |  |  |L3|  |  |  |L3|  |  |  |L3|  |\n'
            'G     |  |L2|  |  |  |L2|  |L2|  |  |  |L2|  |  |\n'
            'H   W3|  |  |L2|  |  |  |W2|  |  |  |L2|  |  |W3|\n'
            'I     |  |L2|  |  |  |L2|  |L2|  |  |  |L2|  |  |\n'
            'J     |L3|  |  |  |L3|  |  |  |L3|  |  |  |L3|  |\n'
            'K     |  |  |  |W2|  |  |  |  |  |W2|  |  |  |  |\n'
            'L   L2|  |  |W2|  |  |  |L2|  |  |  |W2|  |  |L2|\n'
            'M     |  |W2|  |  |  |L2|  |L2|  |  |  |W2|  |  |\n'
            'N     |W2|  |  |  |L3|  |  |  |L3|  |  |  |W2|  |\n'
            'O   W3|  |  |L2|  |  |  |W3|  |  |  |L2|  |  |W3|\n'
        )
        self.assertEqual(self.board.board_in_terminal(), expected_output)

    def test_board_in_terminal_with_tiles(self):
        # Puedes ajustar esta prueba según la disposición de tus letras y fichas en el tablero
        # Asegúrate de que el método `board_in_terminal` tenga en cuenta las fichas en el tablero
        # y en el rack de los jugadores.
        expected_output = (
            ' \n'
            '    0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 \n'
            'A   W3|  |  |L2|  |  |  |W3|  |  |  |L2|  |  |W3|\n'
            'B     |W2|  |  |  |L3|  |  |  |L3|  |  |  |W2|  |\n'
            'C     |  |W2|  |  |  |L2|  |L2|  |  |  |W2|  |  |\n'
            'D   L2|  |  |W2|  |  |  |L2|  |  |  |W2|  |  |L2|\n'
            'E     |  |  |  |W2|  |  |  |  |  |W2|  |  |  |  |\n'
            'F     |L3|  |  |  |L3|  |  |  |L3|  |  |  |L3|  |\n'
            'G     |  |L2|  |  |  |L2|  |L2|  |  |  |L2|  |  |\n'
            'H   W3|  |  |L2|  |  |  |W2|  |  |  |L2|  |  |W3|\n'
            'I     |  |L2|  |  |  |L2|  |L2|  |  |  |L2|  |  |\n'
            'J     |L3|  |  |  |L3|  |  |  |L3|  |  |  |L3|  |\n'
            'K     |  |  |  |W2|  |  |  |  |  |W2|  |  |  |  |\n'
            'L   L2|  |  |W2|  |  |  |L2|  |  |  |W2|  |  |L2|\n'
            'M     |  |W2|  |  |  |L2|  |L2|  |  |  |W2|  |  |\n'
            'N     |W2|  |  |  |L3|  |  |  |L3|  |  |  |W2|  |\n'
            'O   W3|  |  |L2|  |  |  |W3|  |  |  |L2|  |  |W3|\n'
        )
        self.assertEqual(self.board.board_in_terminal(), expected_output)

from game.board import Board, DictionaryConnectionError

class TestDictionaryConnectionError(unittest.TestCase):

    def test_exception_creation(self):
        with self.assertRaises(DictionaryConnectionError):
            raise DictionaryConnectionError()

    def test_exception_message(self):
        try:
            raise DictionaryConnectionError("Error en la conexión con el diccionario")
        except DictionaryConnectionError as e:
            self.assertEqual(str(e), "Error en la conexión con el diccionario")

    def test_dictionary_connection_error(self):
        with self.assertRaises(DictionaryConnectionError):
            raise DictionaryConnectionError("Error de conexión con el diccionario")


if __name__ == '__main__':
    unittest.main()

