import pygame
pygame.init()
w = 1200
h = 700
color = (255,255,255)
screen = pygame.display.set_mode((w,h))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.line(screen, color, (400, 100), (600, 500), 20)
    pygame.display.flip()