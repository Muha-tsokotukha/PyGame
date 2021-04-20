import pygame
import sys
pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
COLOR = (0, 255, 255)
screen = pygame.display.set_mode((720,450))
bg = pygame.image.load('pnt.png')
def main():
    curColor = BLACK
    rect = False
    circle = False
    line = True
    eraser = False
    screen.blit(bg, (0,0))
    while True:
        
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    rect = False
                    circle = False
                    line = True
                    eraser = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if x in range(605,631) and y in range(78,104):
                    rect = True
                    circle = False
                    line = False
                    eraser = False
                if x in range(663,699) and y in range(72,108):
                    rect = False
                    circle = True
                    line = False
                    eraser = False
                if x in range(633,682) and y in range(158,213):
                    rect = False
                    circle = False
                    line = False
                    eraser = True
                if x in range(602,624) and y in range(10,42):
                      curColor = RED
                if x in range(627,652) and y in range(10,42):
                      curColor = GREEN
                if x in range(656,678) and y in range(10,42):
                      curColor = BLUE
                if x in range(682,707) and y in range(10,42):
                      curColor = BLACK
                if x in range(634,683) and y in range(274,325):
                      pygame.draw.rect(screen, WHITE, (586,0 , 720,450))
                      pygame.image.save(screen, 'unnamed.png')
                      pygame.quit()
                      sys.exit()
                
                
                
                
        x1 = pygame.mouse.get_pos()[0]
        if rect and (x1  in range(0,580)):
                if event.type == pygame.MOUSEBUTTONDOWN :
                    prev = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEMOTION:
                    cur = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONUP:
                    pygame.draw.rect(screen, curColor, [min(prev[0],cur[0]), min(prev[1],cur[1]), abs(prev[0]-cur[0]),abs(prev[1]-cur[1]) ],5)
                    prev = (0,0)
        x1 = pygame.mouse.get_pos()[0]
        if circle and (x1  in range(0,580)):
            if event.type == pygame.MOUSEBUTTONDOWN:
                prev = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEMOTION:
                cur = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                pygame.draw.ellipse(screen,curColor, [min(prev[0],cur[0]), min(prev[1],cur[1]), abs(prev[0]-cur[0]),abs(prev[1]-cur[1]) ],5)
                prev = (0,0)
        x1 = pygame.mouse.get_pos()[0]
        y1 = pygame.mouse.get_pos()[1]
        if eraser and (x1 in range(0,540)):
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.circle(screen, WHITE, (x1, y1), 40)
        
        l = False
        if(line) and x1 in range(0,580):
            if event.type == pygame.MOUSEBUTTONDOWN:
                prev = pygame.mouse.get_pos()
                l = True
            if event.type == pygame.MOUSEMOTION:
                cur = pygame.mouse.get_pos()
                if l==True:
                    pygame.draw.line(screen,curColor, prev, cur, 10)
                    prev = cur
            if event.type == pygame.MOUSEBUTTONUP:
                prev = (0,0)



        pygame.display.update()
        pygame.display.flip()

main()