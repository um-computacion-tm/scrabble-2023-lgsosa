from game.scrabble import ScrabbleGame
from game.get_player_count import GetPlayerCount
from game.game_board import Board
from game.game_calculate import Calculate_word_value
from io import StringIO
from game.game_player import Player

class GameComplete:
    def __init__(self):
        print('¡Bienvenido a Scrabble!')
        self.player_count = self.get_player_count()
        self.game = ScrabbleGame(self.player_count)
        self.main_output = StringIO()

    def get_player_count(self):
        player_count = None  # Inicializa player_count como None
        while player_count is None:
            try:
                player_count = int(input('Ingrese la cantidad de jugadores (2-4): '))
                if 2 <= player_count <= 4:
                    self.player_count = player_count  # Configura self.player_count
                else:
                    print('Por favor, ingrese un número entre 2 y 4.')
                    player_count = None  # Reinicia player_count
            except ValueError:
                print('Por favor, ingrese un número válido.')
                player_count = None  # Reinicia player_count


    def show_player(self, current_player):
        print(f"Jugador {current_player + 1}")
        player = self.game.players[current_player - 1]
        print("Rack del jugador:", [tile.letter for tile in player.rack])
        print(f"Puntuación del jugador: {player.score}")

    def get_inputs(self):
        word = input("Ingrese palabra: ")
        coords = (int(input("Ingrese posición X: ")), int(input("Ingrese posición Y: ")))
        orientation = input("Ingrese orientación (V/H): ")
        return word, coords, orientation

    def play(self, word, location, orientation):
        show_board = self.show_board(self.game.board)
        self.game.validate_word(word, location, orientation)
        words = self.game.board.put_words(word, location, orientation)
        total = Calculate_word_value().calculate_word_value(words)
        self.game.players[self.game.current_player].score += total
        self.game.next_turn()

        # Muestra el estado actualizado del tablero después de jugar la palabra
        show_board



    def show_board(self, board):
        for row in board.grid:
            row_str = " | ".join(cell.letter if cell.letter else ' ' for cell in row)
            print(row_str)
            print("-" * len(row_str))

if __name__ == '__main__':
    print('¡Bienvenido a Scrabble!')
    game_complete = GameComplete()

    while game_complete.game.is_playing():
        game_complete.show_board(game_complete.game.board)
        game_complete.show_player(game_complete.game.current_player)
        word, coords, orientation = game_complete.get_inputs()
        try:
            game_complete.play(word, coords, orientation)

            # Muestra el tablero después de jugar una palabra
            game_complete.show_board(game_complete.game.board)

        except ValueError as e:
            print(e)

    print('Fin del juego')

