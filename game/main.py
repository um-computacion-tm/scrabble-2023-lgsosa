from game.scrabble import *
from game.board import *
from game.player import *
import os

class Main():

    def main(self):
        print("Bienvenido a Scrabble")
        while True:
            try:
                players_count = int(input("Ingrese el numero de jugadores 2-4: "))
                if players_count <= 1   or players_count > 4:
                    raise ValueError
                break
            except ValueError:
                print ("Valor no valido")
        return players_count

    def menu(self, menu, scrabble_game):
        show_menu = f'Turno del jugador {scrabble_game.current_player.name}\n\n'
        if menu == 'menu':
            show_menu +=  '''               ¿Qué desea hacer?

    Tablero (1) / Rack (2) / Jugar (3) / Score (4) / Salir (5)

    Seleccion: '''
        elif menu == 'board':
            show_menu +=  '''    ¿Qué desea hacer?

    Ver Tablero (1) / Atras (2)

    Seleccion: '''
        elif menu == 'lectern':
            show_menu +=  '''    ¿Qué desea hacer?

    Ver Rack (1) / Atras (2)
            
    Seleccion: '''
        elif menu == 'actions':
            show_menu += '''    ¿Qué desea hacer?

    Colocar palabra (1) / Cambiar fichas (2) / Pasar (3) / Atrás (4)

    Seleccion: ''' 
        elif menu == 'put_word':
            show_menu += '''    ¿Quiere empezar  a jugar??

    Colocar palabra (1) / Atrás (2)

    Seleccion: '''
        elif menu == 'change_tiles':
            show_menu += '''    ¿Quiere cambiar sus fichas?

    Cambiar fichas / Volver (2)

    Seleccion: '''
        elif menu == 'next_turn':
            show_menu += '''    ¿Realmente quiere pasar turno?

    Pasar turno (1) / Volver (2)
    
    Seleccion: '''
        elif menu == 'scores':
            show_menu += '''    ¿Desea ver sus puntos?

    Ver Score (1) / Atras (2)

    Seleccion: '''
        elif menu == 'exit':
            show_menu += '''    ¿Realmente se quiere ir?

    Salir (1) / Atras (2)

    Seleccion: '''
        return show_menu
   
    def play_game(self, scrabble_game):
        while not scrabble_game.game_over:
            os.system('clear')  # Limpia la pantalla

            # Muestra el tablero y el rack del jugador actual
            print(scrabble_game.view_board())
            for player in scrabble_game.players:
                if player == scrabble_game.current_player:
                    # Es el turno del jugador actual, muestra su rack
                    rack_display = ' | '.join(str(tile) if tile != 'Joker' else 'J' for tile in player.lectern)
                    print(f"Rack del jugador {player.name}: Letras -> {rack_display}")
                else:
                    # No es el turno del jugador, muestra un mensaje genérico
                    print(f"Es el turno de {player.name}. Esperando...")

            try:
                option = int(input(self.menu('menu', scrabble_game)))
                if option == 1:
                    self.menu_board(scrabble_game)
                elif option == 2:
                    self.menu_lectern(scrabble_game)
                elif option == 3:
                    self.menu_actions(scrabble_game)
                elif option == 4:
                    self.menu_scores(scrabble_game)
                elif option == 5:
                    self.menu_salir(scrabble_game)
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Valor no válido")

    def play(self):
        players_count = self.main()
        scrabble_game = ScrabbleGame(players_count=players_count)
        for i in range(players_count):
            name = input("Ingrese el nombre del jugador " + str(i+1) + ": ")
            scrabble_game.players[i].name = name
        scrabble_game.current_player = scrabble_game.players[0]
        self.play_game(scrabble_game)
    
    def menu_board(self, scrabble_game):
        while True:
            option = int(input(self.menu('board', scrabble_game )))
            if option == 1:
                print (scrabble_game.view_board())
            elif option == 2:
                break
            elif option != 1 and option != 2:
                print ('Valor invalido')

    def menu_lectern(self, scrabble_game):
        while True:
            option = int(input(self.menu('lectern', scrabble_game )))
            if option == 1:
                print (scrabble_game.current_player.view_lectern())
            elif option == 2:
                break 
            else:
                print ('Valor invalido')
    
    def menu_actions(self, scrabble_game):
        while True:
            try:
                option = int(input(self.menu('actions', scrabble_game)))
                if option == 1:
                    self.menu_put_word(scrabble_game)
                elif option == 2:
                    self.menu_change_tiles(scrabble_game)
                elif option == 3:
                    value = self.menu_next_turn(scrabble_game)
                    if value == 'cambio de turno':
                        break
                elif option == 4:
                    break
                else:
                    raise ValueError
            except ValueError:
                print ("Valor no valido")
    
    def menu_put_word(self, scrabble_game): 
        word = input('Ingrese una palabra:')
        print(f'Rack del jugador {scrabble_game.current_player.name}: Letras -> {scrabble_game.current_player.view_lectern()}')
        print('Ingrese la coordenada de la fila:')
        row = int(input())
        print('Ingrese la coordenada de la columna:')
        column = int(input())
        location = (row, column)
        print('Ingrese la orientación en la que desea jugar la palabra:')
        print('1. Horizontal')
        print('2. Vertical')
        orientation = int(input())
        
        if orientation == 1:
            orientation = 'H'
        elif orientation == 2:
            orientation = 'V'
        else:
            print('Opción no válida')
            return

        if scrabble_game.board.is_empty():
            if scrabble_game.board.validate(word, location, orientation):
                tiles = scrabble_game.current_player.take_tiles(word)
                scrabble_game.current_player.points += scrabble_game.board.calculate_word_value(word, location, orientation)
                scrabble_game.board.put_word(tiles, location, orientation)
                scrabble_game.current_player.give_tiles(scrabble_game.bag_tiles.take(7 - len(scrabble_game.current_player.lectern)))
                print(scrabble_game.board.board_in_terminal())
            else:
                print('La palabra no es válida o no se puede jugar en esa posición')
        else:
            if scrabble_game.board.validate(word, location, orientation):
                word_without_intersection = scrabble_game.board.get_word_without_intersections(word, location, orientation)
                if scrabble_game.current_player.has_tiles(word_without_intersection):
                    tiles = scrabble_game.current_player.take_tiles(word_without_intersection)
                    scrabble_game.current_player.points += scrabble_game.board.calculate_word_value(word, location, orientation)
                    scrabble_game.board.put_word(tiles, location, orientation)
                    scrabble_game.current_player.give_tiles(scrabble_game.bag_tiles.take(7 - len(scrabble_game.current_player.lectern)))
                    print(scrabble_game.board.board_in_terminal())
                else:
                    print('Usted no tiene las fichas para jugar esa palabra')
            else:
                print('La palabra no es válida o no se puede jugar en esa posición')

        scrabble_game.next_turn()

        

    def menu_change_tiles(self, scrabble_game):
        while True:
            try:
                option = int(input(self.menu('change_tiles', scrabble_game)))
                if option == 1:
                    tiles_index = input("Ingrese los indices de las fichas que desea cambiar: ")
                    print(f'Tiles: {tiles_index}')
                    tiles_index = tiles_index.split(',')
                    tiles_index = [int(i) for i in tiles_index]
                    scrabble_game.change_tiles(tiles_index)
                    print(scrabble_game.current_player.view_lectern())
                    scrabble_game.next_turn()
                    return 'cambio de turno'
                elif option == 2:
                        break
                else:
                    raise ValueError
            except ValueError:
                print ("Valor no valido")

    def menu_next_turn(self, scrabble_game): 
        while True:
            option = int(input(self.menu('next_turn', scrabble_game)))
            if option == 1:
                scrabble_game.next_turn()
                return 'Cambio de turno'
            elif option == 2:
                break
            else:
                print ('Valor invalido')
            
    def menu_scores(self, scrabble_game):
        while True:
            try:
                option = int(input(self.menu('scores', scrabble_game)))
                if option == 1:
                    print(scrabble_game.view_scores())
                elif option == 2:
                    break
                else:
                    raise ValueError
            except ValueError:
                print ("Valor no valido")

    def menu_salir(self, scrabble_game):
        while True:
            try:
                option = int(input(self.menu('exit', scrabble_game)))
                if option == 1:
                    scrabble_game.game_over = True
                    print ("Gracias por jugar\n")
                    break
                elif option == 2:
                    break
                else:
                    raise ValueError
            except:
                print ("Valor no valido")
   
if __name__ == "__main__":
    main = Main()
    main.play()
    main.play_game()

                