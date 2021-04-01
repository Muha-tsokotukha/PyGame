import pygame
pygame.init()
color = (150, 0, 140)
screen = pygame.display.set_mode((500, 500))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()        
    pygame.draw.circle(screen, color, (300, 60), 50, 10)