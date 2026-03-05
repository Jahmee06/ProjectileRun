import pymunk
import pygame

class Projectile():
    #PROJECTILE CLASS
    pass
class Target():
    pass

class Launcher():
    #LOL
    pass


class Projectile_Run():

    #Init function setsup everything
    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode((700,700))
        self.space = pymunk.Space()
        self.space.gravity = (0.0, 900.0)
        self.clock = pygame.time.Clock()

    # Run function updates
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((255, 192, 203))
            self.space.step(1/60)
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()    

