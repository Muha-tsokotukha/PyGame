from Snake import Snake
import pygame 
import time
import random
import pickle

pygame.init()
OLIVE = (10, 40, 20)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255,255,102)
GREEN = (0,255,0)

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake game")

snake_block_size = 10
snake_speed = 20

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("papyrusttc", 50)
score_font = pygame.font.SysFont("ヒラキノ角コシックw0ttc", 35)

FILE_NAME = 'snakes_saved.data'


f = open('1.txt', 'r')
temp1 = f.read()
walls1 = temp1.split('\n')

f2 = open('2.txt', 'r')
temp2 = f2.read()
walls2 = temp2.split('\n')


f3 = open('3.txt', 'r')
temp3 = f3.read()
walls3 = temp3.split('\n')

pos_walls3 = []
i = 1
while i < len(walls3):
    j = 0
    lasty = i
    while j < len(walls3[i]):
            if walls3[i][j] == '#':
                temp = [j,i]
                pos_walls3.append(temp)
            j+=1
    i += 1



pos_walls2 = []
i = 1
while i < len(walls2):
    j = 0
    lasty = i
    while j < len(walls2[i]):
            if walls2[i][j] == '#':
                temp = [j,i]
                pos_walls2.append(temp)
            j+=1
    i += 1

def message(font, msg, color, x, y):
    mesg = font.render(msg, True, color)
    screen.blit(mesg, (x, y))

def game_loop():
    game_over = False
    game_close = False
    choose = False
    lvl = 2
    snake1 = Snake(snake_block_size, BLACK, [WIDTH // 2, HEIGHT // 2])
    keys = {
        'UP': pygame.K_UP,
        'DOWN': pygame.K_DOWN,
        'RIGHT': pygame.K_RIGHT,
        'LEFT': pygame.K_LEFT
    }
    snake2 = Snake(snake_block_size, WHITE, [WIDTH // 2 + 50, HEIGHT // 2], keys=keys)
    while not choose:
        screen.fill(BLACK)
        message(font_style, "Press space to load saved game", WHITE, WIDTH // 8, HEIGHT // 2-50)
        message(font_style, "OR", WHITE, WIDTH // 3+40, HEIGHT // 2 )
        message(font_style, "other button to start a new one", WHITE, WIDTH // 8, HEIGHT // 2+50)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    try:
                        with open(FILE_NAME, 'br') as f:
                            snakes = pickle.load(f)
                    except Exception as e:
                        print(e)
                        snakes = (snake1, snake2)
                else:
                    snakes = (snake1, snake2)
                choose = True
    
    foodx = round(random.randrange(0, WIDTH - snake_block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - snake_block_size) / 10.0) * 10.0
    
    while not game_close:
        clock.tick(snake_speed)

        while game_over:
            screen.fill(BLACK)
            message(font_style, "Game over!", RED, WIDTH //3+30, HEIGHT // 3)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = False
                        game_close = True
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    with open(FILE_NAME, 'bw') as f:
                        pickle.dump(snakes, f)
                    game_close = True

        for snake in snakes:
            x1, y1 = snake.get_head_coordinates()
            if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
                game_over = True
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, WIDTH - snake_block_size) / 10.0) * 10.0
                foody = round(random.randrange(0, HEIGHT - snake_block_size) / 10.0) * 10.0
                snake.add_block()

        pressed_keys = pygame.key.get_pressed()
        for snake in snakes:
            snake.move(pressed_keys)

        screen.fill(OLIVE)
        pygame.draw.rect(screen, GREEN, [foodx, foody, snake_block_size, snake_block_size]) 
        for snake in snakes:
            snake.draw(screen)

        message(score_font, "Your score: " + str(snake1.get_length() - 1), YELLOW, 0, 0)



        if lvl == 2:
            i = 1
            while i < len(walls2):
                j = 0
                lasty = i
                while j < len(walls2[i]):
                    if walls2[i][j] == '#':
                        pygame.draw.line(screen,RED,(j,lasty),(j+1,lasty), 4)
                    j+=1
                i += 1

            
        if lvl == 2:
            for snake in snakes:
                x1, y1 = snake.get_head_coordinates()
                for x in pos_walls2:
                    if x1 == x[0] and y1 == x[1]:
                        game_over = True

        
        if lvl == 3:
            i = 1
            while i < len(walls3):
                j = 0
                lasty = i
                while j < len(walls3[i]):
                    if walls3[i][j] == '#':
                        pygame.draw.line(screen,RED,(j,lasty),(j+1,lasty), 4)
                    j+=1
                i += 1

            
        if lvl == 3:
            for snake in snakes:
                x1, y1 = snake.get_head_coordinates()
                for x in pos_walls3:
                    if x1 == x[0] and y1 == x[1]:
                        game_over = True









        pygame.display.update()
            
    pygame.quit()
    quit()

if __name__ == '__main__':
    game_loop()