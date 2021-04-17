import pygame,random
pygame.init()
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0) 
WHITE = (255, 255,255) 

screen = pygame.display.set_mode((900,600))
colors = [BLACK, RED, GREEN, BLUE]

myfont = pygame.font.SysFont('arial', 60) 
myfont2 = pygame.font.SysFont('arial', 40) 


def drawRectangle(surface, color, x, y, w, h):
    pygame.draw.rect(surface, color, [x, y, w, h], 5)

def drawCircle(surface, color, x, y):
    pygame.draw.circle(surface, color, (x, y), 30, 3)

def drawLine(surface, color, startPos, endPos):
    pygame.draw.line(surface, color, startPos, endPos, 2)

def erase(surface, x, y):
    pygame.draw.circle(surface, WHITE, (x, y), 40)



def main():
    info = True
    while info:
        screen.fill((128,128,128))
        text = myfont.render('Press N to go through tool',True, BLACK)
        screen.blit(text, ( 100, 100))
        text = myfont.render('Press C to go through colors',True,BLACK)
        screen.blit(text, (100, 300))
        text = myfont2.render('Press SPACE to draw/autosave is ON',True, (255,255,255))
        screen.blit(text, (100, 500))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    info = False
                if event.key == pygame.QUIT:
                    pygame.quit()
                    exit()
        pygame.display.flip()
    drawing = True

    
    isPressed = False
    prevPoint = (0, 0)
    curPoint = (0, 0)
    currentTool = 0
    toolCount = 4

    current_color = 0
    colors = (BLUE, GREEN, RED)

    
    screen.fill(WHITE)
    
    while drawing:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    currentTool = (currentTool + 1) % toolCount
                elif event.key == pygame.K_c:
                    current_color = (current_color + 1) % len(colors)
            if event.type == pygame.MOUSEBUTTONDOWN:
                isPressed = True
                prevPoint = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP:
                isPressed = False
            elif event.type == pygame.MOUSEMOTION and isPressed == True:
                prevPoint = curPoint
                curPoint = pygame.mouse.get_pos()
            elif event.type == pygame.QUIT:
                drawing = False
                pygame.image.save(screen, 'unnamed.jpg')
            
        if currentTool == 0:
            drawLine(screen, colors[current_color], prevPoint, curPoint)
        elif currentTool == 1:
            drawRectangle(screen, colors[current_color], curPoint[0], curPoint[1], 100, 100)
        elif currentTool == 2:
            drawCircle(screen, colors[current_color], *curPoint)
        elif currentTool == 3:
            erase(screen, *curPoint)

        pygame.display.flip()
    pygame.display.flip()  
main()