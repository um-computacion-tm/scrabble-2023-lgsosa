import unittest
from unittest.mock import patch
from game.main import *
import io, sys
from game.main import Main
from game.scrabble import ScrabbleGame

class TestMain(unittest.TestCase):
    @patch('builtins.input', side_effect = [2])
    def test_main(self, mock_input):
        main = Main()
        result = main.main()
        self.assertEqual(result, 2)

    @patch('builtins.input', side_effect = [5,2])
    def test_main(self, mock_input):
        main = Main() 
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        result = main.main()
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        output_buffer.close()
        expected = 'Bienvenido a Scrabble\nValor no valido\n'
        self.assertEqual(printed_output, expected)
        self.assertEqual(result, 2)


    @patch('builtins.input', side_effect=[7,2])
    def test_menu_actions_change_tiles_exception(self, mock_input):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main.menu_change_tiles(scrabble_game)
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        output_buffer.close()
        expected = '''Valor no valido\n'''
        self.maxDiff = None
        self.assertEqual(printed_output, expected)

    @patch('builtins.input', side_effect=[1,2])
    def test_menu_actions_next_turn(self, mock_input):
        main = Main ()
        scrabble_game = ScrabbleGame (2)
        scrabble_game.players [0] .name = 'Jugador 1'
        scrabble_game.players [1] .name = 'Jugador 2'
        scrabble_game.next_turn ()
        self.assertEqual(main.menu_next_turn (scrabble_game), 'Cambio de turno')
    
    @patch('builtins.input', side_effect=[7,2])
    def test_menu_actions_next_turn_exception(self, mock_input):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main.menu_next_turn(scrabble_game)
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        output_buffer.close()
        expected = '''Valor invalido\n'''
        self.maxDiff = None
        self.assertEqual(printed_output, expected)

    @patch('builtins.input', side_effect=[1,2])
    def test_menu_actions_scores(self,mock_input):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main.menu_scores(scrabble_game)
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        output_buffer.close()
        expected = '''Jugador 1: 0\nJugador 2: 0\n
'''
        self.maxDiff = None
        self.assertEqual(printed_output, expected)

    @patch('builtins.input', side_effect=[7,2])
    def test_menu_actions_scores_exception(self, mock_input):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main.menu_scores(scrabble_game)
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        output_buffer.close()
        expected = '''Valor no valido\n'''
        self.maxDiff = None
        self.assertEqual(printed_output, expected)

    @patch('builtins.input', side_effect=[1,2])
    def test_menu_board(self,mock_input):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main.menu_board(scrabble_game)
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        output_buffer.close()
        expected = ''' 
    0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 
A   3W|  |  |2L|  |  |  |3W|  |  |  |2L|  |  |3W|
B     |2W|  |  |  |3L|  |  |  |3L|  |  |  |2W|  |
C     |  |2W|  |  |  |2L|  |2L|  |  |  |2W|  |  |
D   2L|  |  |2W|  |  |  |2L|  |  |  |2W|  |  |2L|
E     |  |  |  |2W|  |  |  |  |  |2W|  |  |  |  |
F     |3L|  |  |  |3L|  |  |  |3L|  |  |  |3L|  |
G     |  |2L|  |  |  |2L|  |2L|  |  |  |2L|  |  |
H   3W|  |  |2L|  |  |  |2W|  |  |  |2L|  |  |3W|
I     |  |2L|  |  |  |2L|  |2L|  |  |  |2L|  |  |
J     |3L|  |  |  |3L|  |  |  |3L|  |  |  |3L|  |
K     |  |  |  |2W|  |  |  |  |  |2W|  |  |  |  |
L   2L|  |  |2W|  |  |  |2L|  |  |  |2W|  |  |2L|
M     |  |2W|  |  |  |2L|  |2L|  |  |  |2W|  |  |
N     |2W|  |  |  |3L|  |  |  |3L|  |  |  |2W|  |
O   3W|  |  |2L|  |  |  |3W|  |  |  |2L|  |  |3W|

'''
        self.maxDiff = None
        self.assertEqual(printed_output, expected)


    @patch('builtins.input', side_effect=[7,2])
    def test_menu_lectern_exception(self, mock_input):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main.menu_lectern(scrabble_game)
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        output_buffer.close()
        expected = '''Valor invalido\n'''
        self.maxDiff = None
        self.assertEqual(printed_output, expected)
    
    @patch('builtins.input', side_effect=[1,4])
    def test_menu_actions_1(self,mock_input):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        with patch.object(main, 'menu_put_word') as mock_put_word:
            main.menu_actions(scrabble_game)
            mock_put_word.assert_called_once()


    @patch('builtins.input', side_effect=[2,4])
    def test_menu_actions_2(self,mock_input):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        with patch.object(main, 'menu_change_tiles') as mock_change_tiles:
            main.menu_actions(scrabble_game)
            mock_change_tiles.assert_called_once()
    
    @patch('builtins.input', side_effect=[3,4])
    def test_menu_actions_3(self,mock_input):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        with patch.object(main, 'menu_next_turn') as mock_next_turn:
            main.menu_actions(scrabble_game)
            mock_next_turn.assert_called_once()

    @patch('builtins.input', side_effect=[3,3,4])
    @patch('game.main.Main.menu_next_turn', return_value='cambio de turno')
    def test_menu_actions_3_next_turn(self,mock_input, mock_next_turn):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        main.menu_actions(scrabble_game)

    @patch('builtins.input', side_effect=[7,4])
    def test_menu_actions_exception(self, mock_input):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main.menu_actions(scrabble_game)
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        output_buffer.close()
        expected = '''Valor no valido\n'''
        self.maxDiff = None
        self.assertEqual(printed_output, expected)

    @patch('builtins.input', side_effect=[2, 'Player1', 'Player2', 5])
    def test_play(self, mock_input):
        main = Main()
        main.play()

    @patch('builtins.input', side_effect=[1,2,2,2,3,4,4,2,5,1])
    def test_play_game(self, mock_input):
        main = Main()  
        scrabble_game = ScrabbleGame(2) 
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main.play_game(scrabble_game)
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        output_buffer.close()

    @patch('builtins.input', side_effect=[2, 'Player1', 'Player2', 5,1])
    def test_play(self, mock_input):
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main = Main()
        main.play()
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        output_buffer.close()

    def test_menu_put_word(self):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        
        # Simula el proceso de colocar una palabra válida en el tablero
        with unittest.mock.patch('builtins.input', side_effect=['miPalabra', 1, 1, 1, 1]):
            main.menu_put_word(scrabble_game)
            # Agrega aserciones para verificar que la palabra se coloca correctamente y los puntos se actualizan

        # Simula el proceso de colocar una palabra no válida
        with unittest.mock.patch('builtins.input', side_effect=['miPalabra', 1, 1, 1, 1]):
            main.menu_put_word(scrabble_game)
            # Agrega aserciones para verificar que la función maneja adecuadamente una palabra no válida

        # Simula el proceso de colocar una palabra sin fichas suficientes
        with unittest.mock.patch('builtins.input', side_effect=['miPalabra', 1, 1, 1, 1]):
            main.menu_put_word(scrabble_game)
            # Agrega aserciones para verificar que la función maneja adecuadamente la falta de fichas

    @patch('builtins.input', side_effect=[1])
    def test_menu_salir(self, mock_input):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main.menu_salir(scrabble_game)
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        output_buffer.close()
        self.assertTrue(scrabble_game.game_over)
        self.assertIn("Gracias por jugar", printed_output)
    
    @patch('builtins.input', side_effect=[2])
    def test_main_valid_input(self, mock_input):
        main = Main()
        result = main.main()
        self.assertEqual(result, 2)

    @patch('builtins.input', side_effect=[5, 2])
    def test_main_invalid_input_then_valid_input(self, mock_input):
        main = Main()
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        result = main.main()
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        output_buffer.close()
        expected = 'Bienvenido a Scrabble\nValor no valido\n'
        self.assertEqual(printed_output, expected)
        self.assertEqual(result, 2)

    @patch('builtins.input', side_effect=[2, 1, 2])
    def test_menu_board_as(self, mock_input):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main.menu_board(scrabble_game)
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        output_buffer.close()
        
class TestPlayerAdditional(unittest.TestCase):
    def test_init_with_custom_parameters(self):
        player = Player(name='John', number=1, points=20)
        self.assertEqual(player.name, 'John')
        self.assertEqual(player.number, 1)
        self.assertEqual(player.points, 20)
        self.assertEqual(len(player.lectern), 0)

    def test_change_tiles_with_valid_indices(self):
        player = Player()
        player.give_tiles(['X', 'Y', 'Z'])
        old_tiles = player.change_tiles(old_tiles_index=[2, 3], new_tiles=['A', 'B'])
        self.assertEqual(player.lectern, ['X', 'A', 'B'])
        self.assertEqual(old_tiles, ['Y', 'Z'])

    def test_take_tiles_with_valid_word(self):
        player = Player()
        player.give_tiles(['C', 'A', 'T', 'S', 'R', 'A', 'E'])
        tiles = player.take_tiles('CAT')
        self.assertEqual(tiles, ['C', 'A', 'T'])
        self.assertEqual(player.lectern, ['S', 'R', 'A', 'E'])

    def test_take_tiles_with_invalid_word(self):
        player = Player()
        player.give_tiles(['A', 'B', 'C'])
        tiles = player.take_tiles('DOG')
        self.assertEqual(tiles, [])
        self.assertEqual(player.lectern, ['A', 'B', 'C'])

    def test_view_lectern_with_empty_lectern(self):
        player = Player()
        lectern_str = player.view_lectern()
        self.assertEqual(lectern_str, 'Letras -> ')

    def test_view_lectern_with_non_empty_lectern(self):
        player = Player()
        player.give_tiles(['A', 'B', 'C', 'D'])
        lectern_str = player.view_lectern()
        self.assertEqual(lectern_str, 'Letras -> A | B | C | D')
    
    def test_fill_lectern_with_no_remaining_tiles(self):
        player = Player()
        bag = BagTiles()
        bag.take(100)  # Agotar las fichas en la bolsa
        player.fill(bag)
        self.assertEqual(len(player.lectern), 0)  # El atril debe permanecer vacío

    def has_tiles(self, word):
        # Crear copia del atril del jugador
        lectern_copy = self.lectern[:]
        
        # Recorrer cada letra en la palabra
        for letter in word:
            if letter in lectern_copy:
                lectern_copy.remove(letter)
            else:
                return False  # No se encuentra una letra necesaria en el atril

        return True  # Todas las letras necesarias se encontraron en el atril


    def test_has_tiles_with_invalid_word(self):
        player = Player()
        player.give_tiles(['H', 'E', 'L', 'L', 'O'])
        self.assertFalse(player.has_tiles('GOODBYE'))

    def test_split_word_with_special_characters(self):
        player = Player()
        splited_word = player.split_word('H*E+L/L^O')
        self.assertEqual(splited_word, ['H', '*', 'E', '+', 'L', '/', 'L', '^', 'O'])

    def test_split_word_with_space(self):
        player = Player()
        splited_word = player.split_word('H E L L O')
        self.assertEqual(splited_word, ['H', ' ', 'E', ' ', 'L', ' ', 'L', ' ', 'O'])

if __name__ == '__main__':
    unittest.main()