from game_cell import Cell

def rotate(mat):
    N = len(mat)

class Board:
    def __init__(self):
        self.grid = [
            [Cell(1, '') for _ in range(15)]
            for _ in range(15)
        ]
        for i in range(4):           
            for i in range(7):
                  for j in range (7):
                        if i == 0:
                            self.grid[i][i] = Cell(' ', 3, 'word') 
                        elif i == 5:
                            self.grid[i][i] = Cell(' ', 3, 'letter')
                        elif i == 6:
                            self.grid[i][i] = Cell(' ', 2, 'letter')  
                        else:
                            self.grid[i][i] = Cell(' ', 2, 'word') 
            self.grid[7][0] = Cell(' ', 3, 'word')    
            self.grid[5][1] = Cell(' ', 3, 'letter') 
            self.grid[1][5] = Cell(' ', 3, 'letter')
            self.grid[0][3] = Cell(' ', 2, 'letter') 
            self.grid[3][0] = Cell(' ', 2, 'letter')
            self.grid[6][2] = Cell(' ', 2, 'letter')
            self.grid[2][6] = Cell(' ', 2, 'letter')
            self.grid[7][3] = Cell(' ', 2, 'letter')
            rotate(self.grid)
            self.grid[7][7] = Cell(' ', 2, 'word')