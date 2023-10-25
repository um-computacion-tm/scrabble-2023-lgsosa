"""
from game.main import Main
import unittest
from unittest.mock import patch
from io import StringIO
from game.scrabble import ScrabbleGame
import sys

class TestMain(unittest.TestCase):
    def setUp(self):
        self.main_output = StringIO()
        self.real_stdout = sys.stdout
        sys.stdout = self.main_output

    def tearDown(self):
        sys.stdout = self.real_stdout

    @patch('builtins.input', side_effect=['3'])   
    def test_valid_player_count(self, mock_input):
        main = Main()
        number = "2"
        self.assertEqual(main.valid_player_count(number), True)

    @patch('builtins.input', side_effect=['3'])
    def test_valid_player_count_error(self, mock_input):
        main = Main()
        number = "name"
        self.assertEqual(main.valid_player_count(number), False)

    @patch('builtins.input', side_effect=['3']) 
    def test_player_count_input_valid(self, mock_input):
        main = Main()
        main.play()
        main_output_value = self.main_output.getvalue()
        self.assertIn('Bienvenido', main_output_value)
        self.assertIn('La cantidad de jugadores es: 3', main_output_value)
        self.assertIn('Turno del jugador 1', main_output_value)

    @patch('builtins.input', side_effect=['5', '3'])
    def test_player_count_input_invalid_then_valid(self, mock_input):
        main = Main()
        main.play()
        main_output_value = self.main_output.getvalue()
        self.assertIn('Bienvenido', main_output_value)
        self.assertIn('Valor inválido', main_output_value)
        self.assertIn('La cantidad de jugadores es: 3', main_output_value)
        self.assertIn('Turno del jugador 1', main_output_value)

    def get_player_count():
        while True:
            try:
                player_count = int(input('cantidad de jugadores (1-3): '))
                if player_count <= 3:
                    break
            except Exception as e:
                print('ingrese un numero por favor')

        return player_count

    @patch('builtins.print')
    @patch.object(ScrabbleGame, 'is_playing', side_effect=[True, False])
    @patch.object(ScrabbleGame, 'get_current_player', return_value=(0, "Player",))
    @patch.object(ScrabbleGame, 'play')

    def test_main(self, *args):
        Main()

if __name__ == '__main__':
    unittest.main()
"""