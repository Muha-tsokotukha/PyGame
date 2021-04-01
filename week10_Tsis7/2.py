import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()        
    pygame.draw.circle(screen, (50, 90, 100), (150, 200), 15)