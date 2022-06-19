from game.constants import SQUARE_SIZE

class Square:
    def __init__(self, row, col, pos):
        self.value = 0
        self.row = row
        self.col = col
        self.x, self.y = pos
        self.size = SQUARE_SIZE
    def containsXY(self, x, y):
        if x >= self.x and x <= self.x + self.size and y >= self.y and y <= self.y + self.size:
            return True
        return False
