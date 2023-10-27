from game.scrabble import ScrabbleGame
from game.game_board import Board
from configure_game import Configure

class Main:
    def __init__(self):
        print ("¡Bienvenido a Scrabble!")
        self.player_count = Configure.get_player_count
        self.game = ScrabbleGame(self.player_count)
        self.board = self.game.get_board()
        self.config = Configure
    
    def init_game(self):
        self.config.iniciar_juego
        self.config.get_player_count
        