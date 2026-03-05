import pymunk
import pygame
import random

class Projectile():
    #PROJECTILE CLASS
    pass

class Target():
    def __init__(self, space, position, target_type = "regular"):

        #Keeps targets static
        self.body = pymunk.Body(body_type = pymunk.Body.STATIC)
        self.body.position = position

        #The creates a shape(box)around the target
        self.shape = pymunk.Poly.create_box(self.body, (50, 50))
        self.shape.elasticity = 0.8 # How bouncy it is 

        if target_type ==  "regular":
            self.health = 1
            self.points = 10
            self.color = (0, 255, 0) # Green will change later
        elif target_type == "durable":
            self.health = 2
            self.points = 20
            self.color = (255, 0, 0) # Red will change later
        space.add(self.body, self.shape)

    def draw(self, screen):
        x = self.body.position.x -25
        y = self.body.position.y -25
    
        pygame.draw.rect(screen, self.color, (x, y, 50, 50))


class Launcher():
    #LOL
    pass


class Projectile_Run():

    #Init function sets up everything
    def __init__(self):
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((700,700))
        self.space = pymunk.Space()
        self.space.gravity = (0.0, 900.0)
        self.clock = pygame.time.Clock()

        self.targets = []
        self.targets.append(Target(self.space, (600, 400), "durable"))

    # Run function updates
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((255, 192, 203))
            for target in self.targets:
                target.draw(self.screen)

            self.space.step(1/60)
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()    

game = Projectile_Run()
game.run()

