import pygame
from game.constants import SQUARE_SIZE, WHITE, GREY

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
    def draw(self, win):
        center = SQUARE_SIZE * (1.0/4.0)
        if self.value == 1:
            self.drawX(win, self.x + center, self.y + center )
        else:
            self.drawO(win, self.x + center, self.y + center)
    def drawX(self, win, x, y):
        width = SQUARE_SIZE//2
        height = width
        pygame.draw.aaline(win, WHITE,(x,y),(width+x,height+y))
        pygame.draw.aaline(win, WHITE,(width+x,y),(x,height+y))
    def drawO(self, win, x, y):
        radius = SQUARE_SIZE//4
        width = 3
        pygame.draw.circle(win, WHITE, (x + radius, y + radius), radius)
        pygame.draw.circle(win, GREY, (x + radius, y + radius), radius - width)

    def copy(self):
        square = Square(self.row, self.col, (self.x, self.y))
        square.value = self.value

        return square
