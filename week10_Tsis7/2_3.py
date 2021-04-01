import pygame
pygame.init()

screen = pygame.display.set_mode((480,360))
x = 50
y = 100

done = False
step = 5
while not done:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            done = True
        
    press = pygame.key.get_pressed()
    if press[pygame.K_UP]: y -= step
    if press[pygame.K_DOWN]: y += step
    if press[pygame.K_LEFT]: x -= step
    if press[pygame.K_RIGHT]: x += step 
    if press[pygame.K_SPACE]:
        x = 240
        y = 180 
    if x >= 480:
        x -= 100
    if x <= 0:
        x += 100
    if y >= 360:
        y -= 100
    if y <= 0:
        y += 100
    screen.fill((0,0,0))
    pygame.draw.circle(screen, (140,140,255), (x,y), 40 )    
    pygame.display.flip()
    pygame.time.Clock().tick(60)