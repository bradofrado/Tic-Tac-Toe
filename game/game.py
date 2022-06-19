import pygame
from game.board import Board
from game.constants import ROWS, COLS

class Game:
    def __init__(self, win, playerX, playerO):
        self.PlayerX = playerX
        self.PlayerO = playerO
        self.PlayerX.setPlayer(1)
        self.PlayerO.setPlayer(2)
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
            self.play(self.turn, row, col)
            return self.checkBoard()

    def play(self, player, row, col):
        print('Player ' + player.name + ' played ' + str(row) + ', ' + str(col))
        if self.isValidMove(row, col):
            self.board.play(player.value, row, col)
            self.changeTurn()
        else: 
            print('Invalid move!')
    def checkBoard(self):
        return self.board.checkBoard()
    def isValidMove(self, row, col):
        validSquares = self.board.getValidSquares()
        for square in validSquares:
            if square.row == row and square.col == col:
                return True

        return False

    def changeTurn(self):
        if self.turn.name == 'X':
            self.turn = self.PlayerO
        else:
            self.turn = self.PlayerX

        print('Changed to player ' + self.turn.name)
        pass