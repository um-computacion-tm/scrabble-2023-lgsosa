from game.scrabble import ScrabbleGame
from game.models import Tile
from game.game_board import Board

class Configure:
    def __init__(self):
        print ("¡Bienvenido a Scrabble!")
        self.player_count = self.get_player_count()
        self.game = ScrabbleGame(self.player_count)
        self.board = self.game.get_board()

    def iniciar_juego(self):
        while True:
            try:
                num_players = int(input("Ingrese la cantidad de jugadores: "))
                if num_players <= 1 or num_players > 4:
                    raise ValueError
                break
            except ValueError:
                print("Valor invalido, elegir entre 2-4 jugadores.")
        scrabble_game = ScrabbleGame(players_count = num_players)
        print("Cantidad de jugadores: ", len(scrabble_game.players))
          
    
    def valid_player_count(self,player_count):
        try:
            count = int(player_count)
            return 2<= count <= 4
        except ValueError:
            return False
        
    def get_player_count(self):
        while True:
            player_count = input('Número de participantes es(2-4):')
            if self.valid_player_count(player_count) is True:
                return int(player_count)
            print('Valor ingresado no valido')

    def show_current_player(self):
        player_number = self.game.current_player.id
        print(f'Turno del jugador {player_number}')
    ###
    def show_board(self, board):
        print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(len(board.grid))]))
        for row_index, row in enumerate(board.grid):
            print(
                str(row_index).rjust(2) +
                '| ' +
                ' '.join([repr(cell) for cell in row])
            )
    ###
    def initial_tiles(self):
        self.game.put_initial_tiles_bag()
        self.game.put_tiles_in_rack()
    ###

    def take_turn(self):
        print(f'Tus fichas son: {self.game.show_rack()}')
        while True:
            action = int(input('¿Qué vas hacer? JUGAR(1) / PASAR(2) / PUNTUACION(3): '))
            action = action
            if action == 1:
                self.play()
                break
            elif action == 2:
                break
            elif action == 3:
                self.display_scores()
    def next_turn(self):
        self.game.next_turn()

    def show_scores(self):
        sorted_players = sorted(self.game.players, key=lambda player: player.score, reverse=True) 
        print("Puntajes de los jugadores:")
        for _, player in enumerate(sorted_players, start=1):
            print(f"Jugador {player.id}: Puntaje = {player.score}")

    def place_word(self):
        while True:
            word = input('Ingresar palabra: ')
            location_x = int(input('Ingresar columna (0-14): '))
            location_y = int(input('Ingrese fila (0-14): '))
            location = (location_x, location_y)
            orientation = input('Ingresar (V/H): ')
            if self.game.scrabble_validate_word(word, location, orientation):
                self.game.put_word(word, location, orientation)
                self.add_score(word, location, orientation)
                break
            elif word == 0:
                break
            else:
                print("Valor ingresado no valido ")

    def exchange_tiles(self):
        amount = int(input("¿Cuántas fichas quieres intercambiar? (1-7): "))
        for i in range(amount):
            index = int(input("Elige la ficha que vas a intercambiar (1-7): "))
            self.game.current_player.exchange_tiles(index, self.game.bag_tiles)

    def reorganize(self):
        while True:
            self.game.shuffle_rack()
            print(f'{self.game.show_rack()}')
            organize = input("Si queres terminar apreta la tecla Y sino cualquier tecla ")
            organize = organize.strip().upper()
            if organize == "Y":
                break

    def add_score(self, word, location, orientation):
        self.game.scrabble_word_calculate_score(word, location, orientation)

    def play_game(self):
        print('¡VAMOS A JUGAR!')
        self.initial_tiles()
        self.game.players[0].rack = [Tile('H', 4), Tile('O',1), Tile('L',1), Tile('A',1)]
        self.game.show_board()
        while not self.game.game_over():
            self.next_turn()
            self.show_current_player()
            self.take_turn()
        print('¡SE ACABO LO QUE SE DABA!')
        self.display_final_scores()

if __name__ == "__main__":
    main = Configure()
    game = ScrabbleGame(2)
    main.show_board(main.board)