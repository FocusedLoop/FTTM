import pygame

class Bullet:
    def __init__(self, position_x, position_y, screen):
        self.position_x = position_x + 110
        self.position_y = position_y
        self.screen = screen
        self.laser = pygame.image.load("images/Laser.png")
        self.speed = -10
        self.make = False

    def create(self):
        self.make = True

    def update(self):
        if self.make == True:
            self.position_y += self.speed
            self.screen.blit(self.laser, (self.position_x, self.position_y))
            if self.position_y < 0:
                self.make = False
