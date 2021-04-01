import pygame
import math
pygame.init()
screen = pygame.display.set_mode((1000,650))
x_axis_points = ['-3п', ' 5п', '-2п', ' 3п', '-п ', ' п ', ' 0 ', ' п ', ' п ', ' 3п', ' 2п', ' 5п', ' 3п']
x_axis_points_extra1 = ['', '_ __', '', '_ __', '', '_ _', '', '   _', '', '   __', '', '   __', '']
x_axis_points_extra2 = ['', '  2', '', '  2', '', ' 2', '', ' 2', '', '  2', '', '  2', '']
y_axis_points = [' 1.00', ' 0.75', ' 0.50', ' 0.25', ' 0.00', '-0.25', '-0.50', '-0.75', '-1.00']
font = pygame.font.SysFont('italic', 20)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill((255,255,255))
    #720x480*15px
    #pygame.draw.rect(screen, (0,0,0), (100,10 ,888 ,542), 2) outer lines
    pygame.draw.line(screen, (0,0,0),(100,10),(888,10), 2 )
    pygame.draw.line(screen, (0,0,0),(888,10),(888,542), 2 )
    pygame.draw.line(screen, (0,0,0),(100,10),(100,542), 2 )
    pygame.draw.line(screen, (0,0,0),(100,542),(888,542), 2 )

    pygame.draw.line(screen, (0,0,0),(120,10),(120,542), 1 )    
    pygame.draw.line(screen, (0,0,0),(100,30),(888,30), 1 )    
    pygame.draw.line(screen, (0,0,0),(868,10),(868,542), 1 )
    pygame.draw.line(screen, (0,0,0),(100,522),(888,522), 1 )

    pygame.draw.line(screen, (0,0,0),(499,10),(499,542), 2 ) #x-axis
    pygame.draw.line(screen, (0,0,0),(100,276),(888,276), 2 ) #y-axis
    n = 7
    temp = 84
    while n >0:
        pygame.draw.line(screen, (0,0,0),(120,temp),(868,temp), 1 ) 
        n -= 1
        temp += 64
    n = 5
    temp = 245
    while n > 0:
        pygame.draw.line(screen, (0,0,0),(temp,30),(temp,542), 1 ) 
        n -= 1
        temp+=128
    pygame.draw.line(screen, (0,0,0),(120,56),(128,56), 1 )
    pygame.draw.line(screen, (0,0,0),(120,496),(128,496), 1 )
    n = 6
    temp = 118
    while n > 0 : 
        pygame.draw.line(screen, (0,0,0),(120,temp),(128,temp), 1 )
        n -= 1
        temp += 64

    n = 13
    temp = 100
    while n > 0 :
        pygame.draw.line(screen, (0,0,0),(120,temp),(124,temp), 1 )
        n -= 1
        temp += 32
    pygame.draw.line(screen, (0,0,0),(120,70),(124,70), 1 )
    pygame.draw.line(screen, (0,0,0),(120,44),(124,44), 1 )
    pygame.draw.line(screen, (0,0,0),(120,510),(124,510), 1 )





    for x in range(120, 868):
        sin_y1 = 245 * math.sin((x - 200) / 100 * math.pi)
        sin_y2 = 245 * math.sin((x - 199) / 100 * math.pi)
        pygame.draw.aalines(screen, (255,0,0), False, [(x, 275 + sin_y1), ((x + 1), 275 + sin_y2)])

    for x in range(120, 868, 3):
        cos_y1 = 245 * math.cos((x - 200) / 100 *math.pi)
        cos_y2 = 245 * math.cos((x - 199) / 100 * math.pi)
        pygame.draw.aalines(screen, (0,0,255), False, [(x, 275 + cos_y1), ((x + 1), 275 + cos_y2)])

    screen.blit(font.render('sin(x)', False,(0,0,0)), (600, 45))
    screen.blit(font.render('cos(x)', False, (0,0,0)), (600, 65))
    screen.blit(font.render('X', False, (0,0,0)), (518, 700))


    for x in range(100, 701, 50):
        screen.blit(font.render(x_axis_points[(x - 100) // 50], False, (0,0,0)), (x - 10, 550))
        screen.blit(font.render(x_axis_points_extra1[(x - 100) // 50], False, (0,0,0)), (x - 20, 550))
        screen.blit(font.render(x_axis_points_extra2[(x - 100) // 50], False, (0,0,0)), (x - 10, 570))
    for y in range(40, 521, 60):
        screen.blit(font.render(y_axis_points[(y - 40) // 60], False, (0,0,0)), (25, (y - 10)))



    pygame.display.flip()