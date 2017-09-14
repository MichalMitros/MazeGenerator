import pygame, sys, math
from cell import Cell


class MazeGenerator(object):

    def __init__(self, cellsize):

        self.tps_max = 100.0
        self.width = 600
        self.height = 600
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0
        self.cellsize = cellsize
        self.cols = math.floor(self.width / self.cellsize)
        self.rows = math.floor(self.height / self.cellsize)
        self.grid = []

        for j in range(0, self.rows):
            for i in range(0, self.cols):
                self.grid.append(Cell(self, i, j))

        self.current = self.grid[0]

        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            # Ticking
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1 / self.tps_max

            #Rendering
            self.screen.fill((50, 50, 50))
            self.draw()
            pygame.display.flip()


    def tick(self):
        self.current.visited = True
        self.current.check_neighbors()

    def draw(self):
        for cell in self.grid:
            cell.draw()

if __name__ == "__main__":
    MazeGenerator(40)