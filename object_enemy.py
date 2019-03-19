import pygame

class Enemy:
    def __init__(self, screen, X):
        self.screen = screen
        self.X = X
        self.live = True
        self.Y = 0
        self.XX = self.X + 110
        self.image = pygame.image.load('images/homer.png')

    def move(self):
        self.screen.blit((self.image), (self.X, self.Y))
        self.Y += 1

    def die(self):
        self.X += 1000
        self.Y += 1000
