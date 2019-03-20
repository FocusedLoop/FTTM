import pygame
import random

class Enemy:
    def __init__(self, screen, X):
        self.screen = screen
        self.X = X
        self.spawn = random.randint(0,X)
        self.live = True
        self.Y = 0
        self.XX = self.X + 110
        self.speed = 5
        self.image = pygame.image.load('images/homer.png')
        self.make = False

    def create(self):
        self.make = True

    def move(self):
        if self.make == True:
            self.Y += self.speed
            self.screen.blit((self.image), (self.spawn, self.Y))
            if self.Y < -100:
                self.make = False

    def die(self):
        self.spawn += 10000
        self.Y += 10000
