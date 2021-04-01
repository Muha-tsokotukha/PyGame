import pygame
import math
pygame.init()
screen = pygame.display.set_mode((1000,650))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill((255,255,255))
    #720x480*15px
    
    pygame.draw.line(screen, (0,0,0),(100,10),(888,10), 2 )
    pygame.draw.line(screen, (0,0,0),(888,10),(888,542), 2 )
    pygame.draw.line(screen, (0,0,0),(100,10),(100,542), 2 )
    pygame.draw.line(screen, (0,0,0),(100,542),(888,542), 2 )
    
    pygame.draw.line(screen, (0,0,0),(120,10),(120,542), 1 )
    
    






    pygame.display.flip()