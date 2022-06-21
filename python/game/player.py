import pygame

class Player:
    def __init__(self):
        self.name = ''
    def setPlayer(self, value):
        if value == 1:
            self.name = 'X'
        elif value == 2:
            self.name = 'O'
        self.value = value
    def play(self, board):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'Quit', None
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = board.get_row_col_from_mouse(pos)
                return row, col
        return None, None

class Computer(Player):
    def __init__(self, level = 1):
        self.level = level
        super().__init__()
    def play(self, board):
        return self.minimax(board, self.level, True)[1]
    #score is calculated based on how many squares on a given board can win a game, do win a game, and do stop
    # the other player from winning the game
    def getScore(self, board, player):
        score = 0
        other = (self.value % 2) + 1

        check = board.checkBoard()
        if check == self.value:
            score += 3
        elif check == other:
            score -= 3
        valid = board.getValidSquares()
        for square in valid:
            copy = board.copy()
            copy2 = board.copy()
            copy.play(self.value, square.row, square.col)
            copy2.play(other, square.row, square.col)
            check = copy.checkBoard()
            check2 = copy2.checkBoard()
            if check == self.value:
                score += 1
            if check2 == other:
                score -= 1
        return score
    def minimax(self, board, depth, maxPlayer):
        if depth == 0 or board.checkBoard() != 0:
            player = self.value
            if not maxPlayer:
                player = (self.value % 2) + 1
            return self.getScore(board, player), (None, None)
        if maxPlayer:
            maxEval = float('-inf')
            valid = board.getValidSquares()
            for square in valid:
                copy = board.copy()
                copy.play(self.value, square.row, square.col)
                eval = self.minimax(copy, depth - 1, False)[0]
                maxEval = max(maxEval, eval)
                if maxEval == eval:
                    best_move = (square.row, square.col)
                
            return maxEval, best_move
        else:
            minEval = float('inf')
            valid = board.getValidSquares()
            for square in valid:
                copy = board.copy()
                nextPlayer = (self.value % 2) + 1
                copy.play(nextPlayer, square.row, square.col)
                eval = self.minimax(copy, depth - 1, True)[0]
                minEval = min(minEval, eval)
                if minEval == eval:
                    best_move = (square.row, square.col)
                
            return minEval, best_move

