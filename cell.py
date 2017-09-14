import pygame, math
from pygame.math import Vector2
from random import randint

class Cell(object):

    def __init__(self, game, i, j):
        self.game = game
        self.i = i
        self.j = j
        self.walls = [True, True, True, True]
        self.visited = False

    def highlight(self):
        x = self.i * self.game.cellsize
        y = self.j * self.game.cellsize
        pygame.draw.rect(self.game.screen, (0, 200, 0), pygame.Rect(x, y, self.game.cellsize, self.game.cellsize))

    def draw(self):
        x = self.i*self.game.cellsize
        y = self.j*self.game.cellsize

        color = (255, 255, 255)

        if self.visited:
            pygame.draw.rect(self.game.screen, (160, 0, 160), pygame.Rect(x, y, self.game.cellsize, self.game.cellsize))

        if self.walls[0]:
            p1 = Vector2(x, y)
            p2 = Vector2(x + self.game.cellsize, y)
            pygame.draw.line(self.game.screen, color, p1, p2, 2)

        if self.walls[1]:
            p1 = Vector2(x + self.game.cellsize, y)
            p2 = Vector2(x + self.game.cellsize, y + self.game.cellsize)
            pygame.draw.line(self.game.screen, color, p1, p2, 2)

        if self.walls[2]:
            p1 = Vector2(x + self.game.cellsize, y + self.game.cellsize)
            p2 = Vector2(x, y + self.game.cellsize)
            pygame.draw.line(self.game.screen, color, p1, p2, 2)

        if self.walls[3]:
            p1 = Vector2(x, y + self.game.cellsize)
            p2 = Vector2(x, y)
            pygame.draw.line(self.game.screen, color, p1, p2, 2)

    def index(self, i, j):
        if i < 0 or j < 0 or i > self.game.cols - 1 or j > self.game.rows - 1:
            return self.i + self.j * self.game.cols
        return i + j * self.game.cols

    def check_neighbors(self):
        neighbors = []
        top = self.game.grid[self.index(self.i, self.j - 1)]
        right = self.game.grid[self.index(self.i + 1, self.j)]
        bottom = self.game.grid[self.index(self.i, self.j + 1)]
        left = self.game.grid[self.index(self.i - 1, self.j)]

        if not top.visited:
            neighbors.append(top)
        if not right.visited:
            neighbors.append(right)
        if not bottom.visited:
            neighbors.append(bottom)
        if not left.visited:
            neighbors.append(left)

        if len(neighbors) > 0:
            r = randint(0, len(neighbors)-1)
            return neighbors[r]
        else:
            return False