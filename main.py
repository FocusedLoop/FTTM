import pygame
import time
import object_player
import object_bullet
import object_enemy
import background_space
import scene_menu

def main():
    pygame.init()
    scene_menu.menu()
    screen_width = 1366
    screen_height = 768
    xpos = (screen_width / 2) - 115
    ypos = 575

    logo = pygame.image.load("images/logo.png")
    image = pygame.image.load("images/ship.png")
    background = pygame.image.load("images/space.png")

    space = background_space.Space(screen_height)
    background_size = background.get_size()
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Fly to Space")
    screen = pygame.display.set_mode((background_size), pygame.FULLSCREEN)
    bullet = object_bullet.Bullet(xpos, ypos, screen)
    enemy1 = object_enemy.Enemy(screen, xpos)
    running = True
    bullets = []
    bullet_timer = 0

    while running:
        bullet_timer += 1
        player = object_player.Player(ypos, xpos, screen)

        space.background()
        if space.move == True:
            screen.blit(background, (0, space.background_y))
            screen.blit(background, (0, space.background_y - screen_height))
        screen.blit(image, (xpos,ypos))

        player.move()
        player.shoot()

        if player.go == True:
            if bullet_timer > 30:
                t_bullet = object_bullet.Bullet(xpos, ypos, screen)
                t_bullet.create()
                bullets.append(t_bullet)
                bullet_timer = 0


        for bullet in range(len(bullets)):
            bullets[bullet].update()

        xpos = player.new_pos
        enemy1.move()

        for bullet in range(len(bullets)):
            if bullets[bullet].position_y <= (enemy1.Y + 110) and bullets[bullet].position_x >= enemy1.X and bullets[bullet].position_x <= enemy1.XX:
                bullets[bullet].make = False
                enemy1.die()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == '__main__':
    main()
