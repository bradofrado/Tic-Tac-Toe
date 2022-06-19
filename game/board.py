import pygame
from game.constants import BLACK, WHITE, GREY, RED, SQUARE_SIZE, ROWS, COLS, SPACING, WIDTH
from game.square import Square

class Board:
    def __init__(self):
        # board width = width of 3 squares plus the spacing
        self.boardWidth = COLS * SQUARE_SIZE + (COLS - 1) * SPACING
        self.center = (WIDTH - self.boardWidth)//2
        self.board = self.emptyBoard()
    def draw(self, win):
        win.fill(BLACK)
        self.drawSquares(win)
        self.drawMoves(win)
        pass
    def emptyBoard(self):
        return [[Square(row, col, self.getXY(row, col)) for col in range(COLS)] for row in range(ROWS)]
    def drawSquares(self, win):
        for row in range(ROWS):
            for col in range(COLS):
                x, y = self.getXY(row, col)
                pygame.draw.rect(win, GREY, (x, y, SQUARE_SIZE, SQUARE_SIZE))
    def drawMoves(self, win):
        for row in self.board:
            for square in row:
                if square.value == 0:
                    continue
                square.draw(win)
    def play(self, value, row, col):
        square = self.board[row][col]
        square.value = value
    def getXY(self, row, col):
        yOffset = row * SPACING
        xOffset = col * SPACING + self.center

        x = col*SQUARE_SIZE + xOffset
        y = row*SQUARE_SIZE + yOffset

        return x,y
    def get_row_col_from_mouse(self, pos):
        x, y = pos
        #x -= self.center

        for row in self.board:
            for square in row:
                if square.containsXY(x, y):
                    return square.row, square.col

        return None, None

    def getValidSquares(self):
        squares = []
        for row in self.board:
            for square in row:
                if (square.value == 0):
                    squares.append(square)

        return squares