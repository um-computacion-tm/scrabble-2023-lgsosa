import unittest
from unittest.mock import patch, MagicMock
from game.main import *
import io, sys
from game.main import Main
from game.scrabble import ScrabbleGame
from io import StringIO

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

from unittest import TestCase, mock


class TestMain_more_coverage(unittest.TestCase):

    def setUp(self):
        self.main_instance = Main()


    @patch('builtins.input', side_effect=['2'])
    def test_menu_board_option_2(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            scrabble_game = ScrabbleGame(players_count=2)
            scrabble_game.current_player = scrabble_game.players[0]  # Asegurando que current_player no sea None
            self.main_instance.menu_board(scrabble_game)
            self.assertEqual("", mock_stdout.getvalue())


    @mock.patch('builtins.input', side_effect=['', 'Palabra', '1', '1', '1', '2'])
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_menu_put_word_empty_word(self, mock_stdout, mock_input):
        main_instance = Main()
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.current_player = scrabble_game.players[0]

        main_instance.menu_put_word(scrabble_game)

        expected_output = "La palabra no puede estar vacía\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['2'])
    def test_menu_board_optionss_21(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            scrabble_game = ScrabbleGame(players_count=2)
            scrabble_game.current_player = scrabble_game.players[0]
            self.main_instance.menu_board(scrabble_game)
            self.assertEqual("", mock_stdout.getvalue())

    def test_menu_put_word_invalid_word(self):
        main_instance = Main()
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.current_player = scrabble_game.players[0]

        with patch('builtins.input', side_effect=['InvalidWord', 1, 1, 1, 1]):
            output_buffer = io.StringIO()
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                main_instance.menu_put_word(scrabble_game)

            expected_output = "La palabra no es válida o no se puede jugar en esa posición\n"
            assert expected_output in mock_stdout.getvalue()

    def test_menu_put_word_invalid_position(self):
        main_instance = Main()
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.current_player = scrabble_game.players[0]

        with patch('builtins.input', side_effect=['Scrabble', 1, 1, 1, 2]):
            output_buffer = io.StringIO()
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                main_instance.menu_put_word(scrabble_game)

            expected_output = "La palabra no es válida o no se puede jugar en esa posición\n"
            assert expected_output in mock_stdout.getvalue()

    def test_main_input_validation_intento(self):
        # Simular entrada de usuario
        with patch('builtins.input', side_effect=['5', '3']):
            main_instance = Main()
            result = main_instance.main()
            self.assertEqual(result, 3)

    def test_menu_board_option_intento1(self):
        # Simular entrada de usuario
        with patch('builtins.input', side_effect=['1', '2']):
            scrabble_game = ScrabbleGame(players_count=2)
            main_instance = Main()
            main_instance.menu_board(scrabble_game)  # No hay excepciones esperadas

    @patch('builtins.input', side_effect=['1', '1,2', '2'])
    def test_menu_change_tiles(self, mock_input):
        main_instance = Main()
        scrabble_game = MagicMock()
        scrabble_game.change_tiles = MagicMock()
        scrabble_game.current_player.view_lectern = MagicMock(return_value='A,B,C')
        scrabble_game.next_turn = MagicMock()

        result = main_instance.menu_change_tiles(scrabble_game)

        self.assertEqual(result, 'cambio de turno')
        scrabble_game.change_tiles.assert_called_once_with([1, 2])
        scrabble_game.current_player.view_lectern.assert_called_once()
        scrabble_game.next_turn.assert_called_once()

    @patch('builtins.input', side_effect=['1', '2'])
    def test_menu_next_turn(self, mock_input):
        main_instance = Main()
        scrabble_game = MagicMock()
        scrabble_game.next_turn = MagicMock()

        result = main_instance.menu_next_turn(scrabble_game)

        self.assertEqual(result, 'Cambio de turno')
        scrabble_game.next_turn.assert_called_once()

    @patch('builtins.input', side_effect=['1', '2'])
    def test_menu_scores(self, mock_input):
        main_instance = Main()
        scrabble_game = MagicMock()
        scrabble_game.view_scores = MagicMock(return_value='Scores: 10, 20, 30')

        main_instance.menu_scores(scrabble_game)

        scrabble_game.view_scores.assert_called_once()

    @patch('builtins.input', side_effect=['1', '2'])
    def test_menu_salir(self, mock_input):
        main_instance = Main()
        scrabble_game = MagicMock()
        scrabble_game.game_over = False

        main_instance.menu_salir(scrabble_game)

        self.assertTrue(scrabble_game.game_over)


    @patch('builtins.input', side_effect=['A', '1', '2', '1', '2', '3', '4'])
    def test_menu_put_word(self, mock_input):
        main_instance = Main()
        scrabble_game = MagicMock()
        scrabble_game.current_player.name = 'Player1'
        scrabble_game.view_board = MagicMock(return_value='Board:')
        scrabble_game.current_player.view_lectern = MagicMock(return_value='A, B, C')
        scrabble_game.board.is_empty = MagicMock(return_value=True)
        scrabble_game.board.validate = MagicMock(return_value=True)
        scrabble_game.current_player.take_tiles = MagicMock(return_value=['A', 'B', 'C'])
        scrabble_game.current_player.points = 0
        scrabble_game.board.calculate_word_value = MagicMock(return_value=10)
        scrabble_game.board.put_word = MagicMock()
        scrabble_game.current_player.give_tiles = MagicMock()
        scrabble_game.bag_tiles.take = MagicMock(return_value=['D', 'E'])

        main_instance.menu_put_word(scrabble_game)

        scrabble_game.board.is_empty.assert_called_once()
        scrabble_game.board.validate.assert_called_once_with('A', (1, 2), 'H')
        scrabble_game.current_player.take_tiles.assert_called_once_with('A')
        scrabble_game.board.calculate_word_value.assert_called_once_with('A', (1, 2), 'H')
        scrabble_game.board.put_word.assert_called_once_with(['A', 'B', 'C'], (1, 2), 'H')
        scrabble_game.current_player.give_tiles.assert_called_once_with(['D', 'E'])

    @patch('builtins.input', side_effect=['1'])
    def test_menu_board321(self, mock_input):
        main_instance = Main()
        scrabble_game = MagicMock()
        scrabble_game.current_player.name = 'Player1'
        
        result = main_instance.menu('board', scrabble_game)
        
        self.assertIn('¿Qué desea hacer?', result)
        self.assertIn('Ver Tablero (1) / Atrás (2)', result)
        self.assertIn('Seleccion: ', result)
    
    @patch('builtins.input', side_effect=['2'])
    def test_menu_lectern(self, mock_input):
        main_instance = Main()
        scrabble_game = MagicMock()
        scrabble_game.current_player.name = 'Player1'
        
        result = main_instance.menu('lectern', scrabble_game)
        
        self.assertIn('¿Qué desea hacer?', result)
        self.assertIn('Ver Rack (1) / Atrás (2)', result)
        self.assertIn('Seleccion: ', result)

    @patch('builtins.input', side_effect=['3'])
    def test_menu_actions(self, mock_input):
        main_instance = Main()
        scrabble_game = MagicMock()
        scrabble_game.current_player.name = 'Player1'
        
        result = main_instance.menu('actions', scrabble_game)
        
        self.assertIn('¿Qué desea hacer?', result)
        self.assertIn('Colocar palabra (1) / Cambiar fichas (2) / Pasar (3) / Atrás (4)', result)
        self.assertIn('Seleccion: ', result)

class TestMain_coveragerrr(unittest.TestCase):
    def setUp(self):
        self.main_instance = Main()
        self.scrabble_game = MagicMock()
        self.scrabble_game.game_over = False
        self.player_mock = MagicMock()
        self.scrabble_game.players = [self.player_mock]
        self.scrabble_game.view_board = MagicMock(return_value='Board:')
        self.player_mock.name = 'Player1'
        self.player_mock.lectern = ['A', 'B', 'C']
        self.board = Board()
        
    def test_board_in_terminal(self):
        with patch('builtins.input', side_effect=['0', '0']):
            terminal_output = self.board.board_in_terminal()
        self.assertTrue('A' in terminal_output)
        self.assertTrue('B' in terminal_output)
        self.assertTrue('C' in terminal_output)

    def test_add_multipliers(self):
        self.board.add_multipliers()
        # Add assertions to check that the multipliers are correctly set on the board

    def test_get_cells(self):
        pos = (1, 2)
        i = 3
        horizontal = True
        cell, invert_cell, side_cell = self.board.get_cells(pos, i, horizontal)
        # Add assertions to check the values of cell, invert_cell, and side_cell

    def test_get_side_word(self):
        cell = self.board.grid[1][1]
        i = 2
        orientation = (True, False)
        pos = (3, 2)
        letter = 'X'
        side_word, j = self.board.get_side_word(cell, i, orientation, pos, letter)
        # Add assertions to check the values of side_word and j

    def test_get_letter_value(self):
        letter_value = self.board.get_letter_value('A')
        self.assertEqual(letter_value, 1)  # Add more assertions for other letters

    def test_update_multipliers(self):
        cell = self.board.grid[1][1]
        letter_value = 3
        word_multiplier = 2
        points = 10
        first = True
        new_word_multiplier, new_points = self.board.update_multipliers(cell, letter_value, word_multiplier, points, first)
        # Add assertions to check the values of new_word_multiplier and new_points

    def test_validate_word_inside_board(self):
        word = 'TEST'
        location = (1, 1)
        orientation = 'H'
        result = self.board.validate_word_inside_board(word, location, orientation)
        self.assertTrue(result)

    def test_words_with_accent(self):
        word = 'ÁÉÍÓÚ'
        result = self.board.words_with_accent(word)
        self.assertEqual(result, 'AEIOU')

    def test_get_word_without_intersections(self):
        word = 'PYTHON'
        pos = (5, 5)
        horizontal = True
        result = self.board.get_word_without_intersections(word, pos, horizontal)
        # Add assertions to check the result

    def test_validate_worrrd(self):
        # Test the validate_word method
        word = "VALID"
        with patch('game.board.dle.search_by_word', MagicMock(return_value=MagicMock(meta_description=''))):
            result = self.board.validate_word(word)
            # Add an assertion to verify that the result is True
            self.assertTrue(result)

    def test_put_word_vertical(self):
        # Verifica que se coloque correctamente una palabra en la dirección vertical
        self.board.put_word('VERT', (5, 5), 'V')
        self.assertEqual(self.board.grid[5][5].tile, 'V')

    def test_words_with_accent_uppercase(self):
        # Asegura que las palabras con acentos en mayúsculas se conviertan correctamente
        result = self.board.words_with_accent('áéíóú')
        self.assertEqual(result, 'AEIOU')


if __name__ == '__main__':
    unittest.main()

