
from game.scrabble import ScrabbleGame
from game.get_player_count import GetPlayerCount
from game.game_board import Board
from game.game_calculate import Calculate_word_value
from io import StringIO
from game.game_player import Player

class game_complete:
    def __init__(self):
        print('¡Bienvenido a Scrabble!')
        self.player_count = self.get_player_count()
        self.game = ScrabbleGame(self.player_count)
        self.main_output = StringIO()

    def show_player(self,current_player):
        print(f"Jugador {current_player + 1}") 
        # Ahora debes encontrar la instancia de Player correspondiente a current_player
        player = self.player_count[current_player - 1]  # Suponiendo que los jugadores están numerados desde 1
        print("Rack del jugador:", [tile.letter for tile in player.rack])
        print(f"Puntuación del jugador: {player.score}")

    def get_inputs():
        word = input("Ingrese palabra: ")
        coords = (int(input("Ingrese posición X: ")), int(input("Ingrese posición Y: ")))
        orientation = input("Ingrese orientación (V/H): ")
        return word, coords, orientation

    def play(self, word, location, orientation, Board):
        show_board = Board(show_board)
        self.validate_word(word, location, orientation)
        words = self.board.put_words(word, location, orientation)
        total = Calculate_word_value().calculate_word_value(words)
        self.players[self.current_player].score += total
        self.next_turn()

        # Muestra el estado actualizado del tablero después de jugar la palabra
        show_board(self.board)

    def get_player_count(self):
        while True:
            try:
                player_count = int(input('Ingrese la cantidad de jugadores (2-4): '))
                if 2 <= player_count <= 4:
                    return player_count
                else:
                    print('Por favor, ingrese un número entre 2 y 4.')
            except ValueError:
                print('Por favor, ingrese un número válido.')
    
    def show_board(board):
        for row in board.grid:
            row_str = " | ".join(cell.letter if cell.letter else ' ' for cell in row)
            print(row_str)
            print("-" * len(row_str))


    if __name__ == '__main__':
        player_count = get_player_count()  # Llama a la función para obtener la cantidad de jugadores
        game = ScrabbleGame(player_count)

        while game.is_playing():
            show_board(game.board)  # Muestra el tablero al comienzo de cada turno
            show_player(game.current_player)  # Muestra el jugador actual
            word, coords, orientation = get_inputs()
            try:
                game.play(word, coords, orientation)

                # Muestra el tablero después de jugar una palabra
                show_board(game.board)

            except ValueError as e:
                print(e)

        print('Fin del juego')
