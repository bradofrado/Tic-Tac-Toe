class Game:
    def __init__(self, win, playerX, playerO):
        self.PlayerX = playerX
        self.PlayerO = playerO

        self.PlayerX.name = 'X'
        self.PlayerO.name = 'O'

        self.turn = self.PlayerX
        pass
    def winner(self):
        return None

    def update(self):
        pass
    
    def playNextTurn(self):
        if self.turn.play():
            self.changeTurn()

    def changeTurn(self):
        if self.turn.name == 'X':
            self.turn = self.PlayerO
        else:
            self.turn = self.PlayerX

        print('Changed to player ' + self.turn.name)
        pass