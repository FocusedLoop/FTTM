import pygame

pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

bullets = []

background = pygame.image.load("space.png").convert()
ship = pygame.image.load("Ship.png").convert_alpha()
ship = pygame.transform.scale(ship, (64, 64))
bulletpicture = pygame.image.load("Laser.png").convert_alpha()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            bullets.append([event.pos[0]-3, 500])

    clock.tick(60)

    mx, my = pygame.mouse.get_pos()

    for b in range(len(bullets)):
        bullets[b][1] -= 10

    # Iterate over a slice copy if you want to mutate a list.
    for bullet in bullets[:]:
        if bullet[0] < 0:
            bullets.remove(bullet)

    screen.blit(background, (0, 0))

    for bullet in bullets:
        screen.blit(bulletpicture, pygame.Rect(bullet[0], bullet[1], 0, 0))

    screen.blit(ship, (mx-32, 500))
    pygame.display.update()
