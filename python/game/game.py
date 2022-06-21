import pygame
from game.board import Board
from game.constants import ROWS, COLS, WHITE, RED

class Game:
    def __init__(self, win, playerX, playerO):
        self.PlayerX = playerX
        self.PlayerO = playerO
        self.PlayerX.setPlayer(1)
        self.PlayerO.setPlayer(2)

        self.turn = None
        self.changeTurn()

        self.board = Board()

        pygame.font.init()
        self.font = pygame.font.SysFont(None, 30)

        self.win = win
        self.status = None
        pass
    def winner(self):
        return self.status

    def update(self):
        self.board.draw(self.win)
        self.writeText(self.text)
        pygame.display.update()
    
    def writeText(self, text):
        color = WHITE
        if self.status == 'Winner':
            color = RED
        textSurface = self.font.render(text, True, color)
        self.win.blit(textSurface, (50,350))
    def playNextTurn(self):
        row, col = self.turn.play(self.board)
        if row == 'Quit':
            return row
        if self.status == 'Winner':
            return

        if row != None:
            self.play(self.turn, row, col)
            value = self.checkBoard()

            if value == 1:
                self.text = 'Player X wins!'
                self.status = 'Winner'
                return self.status
            if value == 2:
                self.text = 'Player O wins!'
                self.status = 'Winner'
                return self.status
            elif value == -1:
                self.text = 'Nobody wins :('


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
        if self.turn and self.turn.name == 'X':
            self.turn = self.PlayerO
        else:
            self.turn = self.PlayerX

        print('Changed to player ' + self.turn.name)
        self.text = 'Player ' + self.turn.name + '\'s turn'