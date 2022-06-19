import pygame
from game.board import Board

class Game:
    def __init__(self, win, playerX, playerO):
        self.PlayerX = playerX
        self.PlayerO = playerO
        self.PlayerX.name = 'X'
        self.PlayerO.name = 'O'
        self.turn = self.PlayerX

        self.board = Board()
        
        self.win = win
        pass
    def winner(self):
        return None

    def update(self):
        self.board.draw(self.win)
        pygame.display.update()
    
    def playNextTurn(self):
        row, col = self.turn.play(self.board)
        if row == 'Quit':
            return row
            
        if row != None:
            print('Player ' + self.turn.name + ' played ' + str(row) + ', ' + str(col))
            self.changeTurn()

    def changeTurn(self):
        if self.turn.name == 'X':
            self.turn = self.PlayerO
        else:
            self.turn = self.PlayerX

        print('Changed to player ' + self.turn.name)
        pass