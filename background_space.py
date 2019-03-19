import pygame
class Space:
    def __init__(self, screen_height):
        self.move = False
        self.screen_height = screen_height
        self.background_speed = 10
        self.background_y = 0

    def background(self):
        pygame.init()

        self.background_y += self.background_speed
        if self.background_y >= self.screen_height:
            self.background_y = 0
        else:
            self.move = True
        pygame.display.update()
