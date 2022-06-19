import pygame
from game.game import Game
from game.constants import WIDTH, HEIGHT
from game.player import Player

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN, Player(), Player())

    while run:
        clock.tick(FPS)

        if game.winner() != None:
            print(game.winner())
            run = False

        status = game.playNextTurn()

        if status == 'Quit':
            run = False

        game.update()
    
    pygame.quit()

main()