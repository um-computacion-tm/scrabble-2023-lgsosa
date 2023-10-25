import unittest
from game_complete import GameComplete


class TestGameComplete(unittest.TestCase):
    def setUp(self):
        # Configura el estado inicial para cada prueba si es necesario
        self.game_complete = GameComplete()

    def test_get_player_count_valid(self):
        # Prueba el método get_player_count con un valor válido
        player_count = self.game_complete.get_player_count()
        self.assertEqual(player_count, 2)  # Cambia 2 por el valor esperado

    def test_get_player_count_invalid(self):
        # Prueba el método get_player_count con un valor inválido
        # Simula la entrada del usuario con un valor inválido
        with unittest.mock.patch('builtins.input', side_effect=['1', '5', '3']):
            player_count = self.game_complete.get_player_count()
            self.assertEqual(player_count, 3)  # Cambia 3 por el valor esperado

    def test_validate_word_valid(self):
        # Prueba el método validate_word con una palabra válida
        word = "HELLO"
        location = (7, 7)
        orientation = "H"
        result = self.game_complete.game.validate_word(word, location, orientation)
        self.assertTrue(result)  # Asegúrate de que el resultado sea True

    def test_validate_word_invalid(self):
        # Prueba el método validate_word con una palabra inválida
        word = "INVALID"
        location = (7, 7)
        orientation = "H"
        with self.assertRaises(ValueError):
            self.game_complete.game.validate_word(word, location, orientation)

if __name__ == '__main__':
    unittest.main()

