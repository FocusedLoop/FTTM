import pygame

class Player:
    def __init__(self, position_y, position_x, screen):
        pygame.init()
        self.position_y = position_y
        self.position_x = position_x
        self.screen = screen
        self.speed = 0
        self.new_pos = self.position_x
        self.bulletpicture = pygame.image.load("images/laser.png").convert_alpha()
        self.go = False

    def move(self):
        pygame.init()
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            self.speed += +10
        if key[pygame.K_a]:
            self.speed += -10
        if self.position_x + self.speed < (1366 - 200) and self.position_x + self.speed > 0:
            self.new_pos = self.position_x + self.speed

    def shoot(self):
        pygame.init()
        key = pygame.key.get_pressed()
        if key[pygame.K_e]:
            self.go = True
