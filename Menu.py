import pygame
import time

def Menue():
    pygame.init()
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 100)
    screen_width = 1366
    screen_height = 768
    number = 4
    logo = pygame.image.load("logo.png")
    background = pygame.image.load("Moon.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Fly to Space")
    screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
    start = pygame.image.load("Start.png").convert()
    start_x = screen_width / 2 - 160
    start_y = 200
    pygame.display.flip()
    running = True

    while running:
        pygame.display.update()
        screen.blit(background, [0,0])
        screen.blit(start ,(start_x,start_y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                while number != 1:
                    number -= 1
                    textsurface = myfont.render(str(number), False, (255, 255, 255))
                    screen.fill([0,0,0])
                    screen.blit(textsurface,(650, 300))
                    pygame.display.flip()
                    time.sleep(1)
                running = False
