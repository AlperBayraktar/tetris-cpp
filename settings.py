class PYGAME_SCREEN:
    # If FULL_SCREEN is True, SCREEN_SIZE doesn't matter.
    # If FULL_SCREEN is False, SCREEN_SIZE determines size of screen.
    FULL_SCREEN = True
    SCREEN_SIZE = None
    TITLE = "Tetris by Alper Bayraktar"


class GAME_GRID:
    ROW_COUNT = 16
    COLUMN_COUNT = 10

class SQUARE:
    SIDE_LENGTH = 30 # pixels 

class COLORS:
    GRID_SEPERATOR = (128, 128, 128)
    SQUARE = (0, 0, 0)

    RED = (255, 0, 0)