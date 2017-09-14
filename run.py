import pygame, sys, math
from cell import Cell

# Use UP/DOWN ARROWS to change speed
# Use SPACE to create new maze

class MazeGenerator(object):

    def __init__(self, cellsize):

        self.tps_max = 7.0
        self.width = 600
        self.height = 600
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('MazeGenerator')
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0
        self.cellsize = cellsize
        self.cols = math.floor(self.width / self.cellsize)
        self.rows = math.floor(self.height / self.cellsize)
        self.grid = []
        self.stack = []
        self.is_running = True

        for j in range(0, self.rows):
            for i in range(0, self.cols):
                self.grid.append(Cell(self, i, j))

        self.current = self.grid[0]

        while self.is_running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.is_running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    self.tps_max += 1.0
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and self.tps_max > 1.0:
                    self.tps_max -= 1.0

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
        next_cell = self.current.check_neighbors()
        if next_cell != False:
            next_cell.visited = True
            self.stack.append(self.current)
            self.remove_walls(self.current, next_cell)
            self.current = next_cell
        elif len(self.stack) > 0:
            self.current = self.stack.pop()

    def draw(self):
        for i in range(0, len(self.grid) - 1):
            self.grid[i].draw()
        self.current.highlight()

    def remove_walls(self, a, b):
        x = a.i - b.i
        if x == 1:
            a.walls[3] = False
            b.walls[1] = False
        elif x == -1:
            a.walls[1] = False
            b.walls[3] = False

        y = a.j - b.j
        if y == 1:
            a.walls[0] = False
            b.walls[2] = False
        elif y == -1:
            a.walls[2] = False
            b.walls[0] = False


if __name__ == "__main__":
    while True:
        MazeGenerator(20)