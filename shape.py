from types import FunctionType
import pygame
from square import SQUARE_STATUS, SquareGridLocation
from settings import COLORS
from square import Square

class SHAPE_MOVES:
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"

class Shape:
    def __init__(self, name: str, squareLocations: list, squareGrid: list, color: tuple) -> None:
        self.name = name
        
        self.squareLocations = []
        for squareLocation in squareLocations:
            self.squareLocations.append(SquareGridLocation(squareLocation[0], squareLocation[1]))    

        self.squareGrid = squareGrid
        self.color = color

        # Setup
        for squareLocation in self.squareLocations:
            square = self.getSquare(squareLocation)
            square.setColor(pygame.Color(self.color))
            square.setStatus(SQUARE_STATUS.FILLED)

    def getSquare(self, location: SquareGridLocation) -> Square:
        return self.squareGrid[location.y][location.x]

    def render(self, window: pygame.Surface, renderSeperators: FunctionType):
        for squareLocation in self.squareLocations:
            self.getSquare(squareLocation).render(window)

        renderSeperators()

    def move(self, rotation: str, window: pygame.Surface):
        for squareLocation in self.squareLocations:
                square = self.getSquare(squareLocation)
                square.setColor(pygame.Color(COLORS.SQUARE))
                square.setStatus(SQUARE_STATUS.EMPTY)
                square.render(window)
        
        if rotation == SHAPE_MOVES.DOWN:
            for squareLocation in self.squareLocations:
                squareLocation.y += 1
        elif rotation == SHAPE_MOVES.RIGHT:
            for squareLocation in self.squareLocations:
                squareLocation.x += 1
        elif rotation == SHAPE_MOVES.LEFT:
            for squareLocation in self.squareLocations:
                squareLocation.x -= 1

        for squareLocation in self.squareLocations:
                square = self.getSquare(squareLocation)
                square.setColor(pygame.Color(self.color))
                square.setStatus(SQUARE_STATUS.FILLED)
                square.render(window)