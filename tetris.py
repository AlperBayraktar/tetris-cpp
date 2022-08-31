import pygame
from square import Square
from shape import Shape, SHAPE_MOVES
from settings import GAME_GRID, SQUARE, COLORS

class Tetris:
    def __init__(self, window: pygame.Surface) -> None:
        self.window = window
        self.setupSquareGrid()
        self.renderGridSquares()
        self.renderGridSeperators()
        
        self.shapes = [
            Shape("I", [
                (0, 0),
                (0, 1),
                (0, 2)
            ],
            self.squareGrid,
            COLORS.RED)
        ]

        self.currentShape = self.shapes[0]
        self.renderShape(self.currentShape)
        pygame.display.update()

    def setupSquareGrid(self) -> None:
        # Creates a two dimensional array of squares
        self.squareGrid = []
        self.gridStartingPosition = {"x": 100, "y": 35}
        
        for row_index in range(GAME_GRID.ROW_COUNT):
            row = []
            
            for col_index in range(GAME_GRID.COLUMN_COUNT):
                square = Square()
                square.location.updateCoordinates(self.gridStartingPosition["x"] + col_index * SQUARE.SIDE_LENGTH,
                                      self.gridStartingPosition["y"] + row_index * SQUARE.SIDE_LENGTH)
                square.setColor(pygame.Color(COLORS.SQUARE))
                row.append(square)

            self.squareGrid.append(row)

    def renderGridSquares(self) -> None:
        # Render every square
        for row in self.squareGrid:
            for square in row:
                square.render(self.window)


    def renderGridSeperators(self) -> None:
        # Render seperator lines
        for row_index in range(GAME_GRID.ROW_COUNT + 1):
            # Draw horizontal lines to seperate every row
            horizontalLineY = row_index * SQUARE.SIDE_LENGTH + self.gridStartingPosition["y"]
            pygame.draw.line(
                            self.window, 
                            
                            pygame.Color(COLORS.GRID_SEPERATOR),
                            
                            (
                                self.gridStartingPosition["x"], 
                                horizontalLineY
                            ), 
                            
                            (
                                self.gridStartingPosition["x"] + GAME_GRID.COLUMN_COUNT * SQUARE.SIDE_LENGTH,
                                horizontalLineY
                            )
            )

            for col_index in range(GAME_GRID.COLUMN_COUNT + 1):
                verticalLineX = self.gridStartingPosition["x"] + col_index * SQUARE.SIDE_LENGTH
                
                # Draw vertical lines for each column to seperate each one in this current row
                pygame.draw.line(
                    self.window,
                    
                    pygame.Color(COLORS.GRID_SEPERATOR),
                    
                    (
                        verticalLineX,
                        self.gridStartingPosition["y"]
                    ),

                    (
                        verticalLineX,
                        self.gridStartingPosition["y"] + GAME_GRID.ROW_COUNT * SQUARE.SIDE_LENGTH
                    )
                )


    def renderShape(self, shape: Shape) -> None:
        shape.render(self.window, self.renderGridSeperators)

    def cycle(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()

                if event.key in [pygame.K_a, pygame.K_LEFT]:
                    self.currentShape.move(SHAPE_MOVES.LEFT, self.window)

                elif event.key in [pygame.K_d, pygame.K_RIGHT]:
                    self.currentShape.move(SHAPE_MOVES.RIGHT, self.window)

                elif event.key in [pygame.K_s, pygame.K_DOWN]:
                    self.currentShape.move(SHAPE_MOVES.DOWN, self.window)

        self.currentShape.move(SHAPE_MOVES.DOWN, self.window)
        
        self.renderShape(self.currentShape)
        pygame.display.flip()