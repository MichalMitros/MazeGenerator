import pygame
from pygame.math import Vector2

class Cell(object):

    def __init__(self, game, i, j):
        self.game = game
        self.i = i
        self.j = j
        self.walls = [True, True, True, True]
        self.visited = False

    def tick(self):
        pass

    def draw(self):
        x = self.i*self.game.cellsize
        y = self.j*self.game.cellsize

        color = (255, 255, 255)

        if self.visited:
            color = (255, 0, 255)
            pygame.draw.rect(self.game.screen, (128, 0, 128), pygame.Rect(x, y, x + self.game.cellsize, y + self.game.cellsize))

        if self.walls[0]:
            p1 = Vector2(x, y)
            p2 = Vector2(x + self.game.cellsize, y)
            pygame.draw.line(self.game.screen, color, p1, p2, 3)

        if self.walls[1]:
            p1 = Vector2(x + self.game.cellsize, y)
            p2 = Vector2(x + self.game.cellsize, y + self.game.cellsize)
            pygame.draw.line(self.game.screen, color, p1, p2, 3)

        if self.walls[2]:
            p1 = Vector2(x + self.game.cellsize, y + self.game.cellsize)
            p2 = Vector2(x, y + self.game.cellsize)
            pygame.draw.line(self.game.screen, color, p1, p2, 3)

        if self.walls[3]:
            p1 = Vector2(x, y + self.game.cellsize)
            p2 = Vector2(x, y)
            pygame.draw.line(self.game.screen, color, p1, p2, 3)

    def check_neighbors(self):
        neighbors = []
        index = self.i + (self.j)-1 * self.game.cols
        right = self.game.grid[index]