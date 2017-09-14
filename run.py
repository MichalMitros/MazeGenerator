import pygame, sys

class MazeGenerator(object):

    def __init__(self):

        self.tps_max = 100.0
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

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
        pass

    def draw(self):
        pass

if __name__ == "__main__":
    MazeGenerator()