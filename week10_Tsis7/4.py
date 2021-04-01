import pygame
pygame.init()
color = (255, 255, 255)
screen = pygame.display.set_mode((500, 500))
x = 30
y = 50
step = 2
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()    
    if pressed[pygame.K_UP]: y -= step
    if pressed[pygame.K_DOWN]: y += step
    if pressed[pygame.K_LEFT]: x -= step
    if pressed[pygame.K_RIGHT]: x += step
    screen.fill((0,0,0))        
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 100, 100), 10)
    pygame.display.flip()
    pygame.time.Clock().tick(60)