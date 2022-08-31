import pygame
from settings import COLORS, SQUARE

class SQUARE_STATUS:
    EMPTY = "EMPTY"
    FILLED = "FILLED"

# This holds x,y coordinates of grid
class SquareGridLocation:
    def __init__(self, x: int, y:int) -> None:
        self.updateCoordinates(x, y)

    def updateCoordinates(self, x: int, y:int) -> None:
        self.x, self.y = x, y

# This holds x,y coordinates of window
class SquareLocation(SquareGridLocation):
    pass

class Square:
    def __init__(self) -> None:
        self.location = SquareLocation(0,0)
        self.setColor(pygame.Color(COLORS.SQUARE))
        self.setStatus(SQUARE_STATUS.EMPTY)

    def setColor(self, color) -> None:
        self.color = color

    def setStatus(self, newStatus) -> None:
        self.status = newStatus

    def render(self, window) -> None:
        pygame.draw.rect(
            window,
            self.color,
            pygame.Rect(self.location.x, self.location.y, SQUARE.SIDE_LENGTH, SQUARE.SIDE_LENGTH),
            0)