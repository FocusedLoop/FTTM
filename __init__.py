import pygame
from FTTM.Player import Player
from FTTM.Bullet import Bullet
from FTTM.Enemy import enemy
from FTTM.Space import Space
from FTTM.Menu import menue

def main():
    menue()
    pygame.init()
    screen_width = 1366
    screen_height = 768
    xpos = (screen_width / 2) - 115
    ypos = 575

    logo = pygame.image.load("logo.png")
    image = pygame.image.load("Ship.png")
    background = pygame.image.load("space.png")

    space = Space(screen_height)
    background_size = background.get_size()
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Fly to Space")
    screen = pygame.display.set_mode((background_size), pygame.FULLSCREEN)
    bullet = Bullet(xpos, ypos, screen)
    enemy1 = enemy(screen, xpos)
    running = True

    while running:
        player = Player(ypos, xpos, screen)
        space.background()
        if space.move == True:
            screen.blit(background, (0, space.background_y))
            screen.blit(background, (0, space.background_y - screen_height))
        screen.blit(image, (xpos,ypos))
        player.move()
        player.shoot()
        if player.go == True:
            bullet = Bullet(xpos, ypos, screen)
            bullet.create()
        bullet.update()
        xpos = player.new_pos
        enemy1.move()
        if bullet.position_y <= (enemy1.Y + 110) and bullet.position_x >= enemy1.X and bullet.position_x <= enemy1.XX:
            bullet.make = False
            enemy1.die()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    main()