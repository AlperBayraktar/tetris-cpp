import pygame
pygame.init()

from tetris import Tetris
from settings import PYGAME_SCREEN


# Init screen
if PYGAME_SCREEN.FULL_SCREEN:
    setModeKwargs = {}
    pygame.mouse.set_visible(False)
else:
    setModeKwargs = {
        "size": PYGAME_SCREEN.SCREEN_SIZE
    }

pygame.display.set_caption(PYGAME_SCREEN.TITLE)
window = pygame.display.set_mode(**setModeKwargs)
game = Tetris(window)

while True:
    game.cycle()
    pygame.time.delay(150)
