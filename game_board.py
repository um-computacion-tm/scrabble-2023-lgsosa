class Board:
    def _init_(self):
        self.grid = [
            [None for _ in range (15)
             for _ in range (15)] #cada elemento de la columna por cada elemento de la fila (none) genera un elemento con none
        ]