import pygame

class Player:
    def __init__(self):
        self.name = ''
    def play(self, board):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'Quit', None
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = board.get_row_col_from_mouse(pos)
                return row, col
        return None, None