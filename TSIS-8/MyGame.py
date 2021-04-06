import pygame
import random
import time

pygame.init()
menuScore = 0
# Colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen
WIDTH = 400
HEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

# Background
BACKGROUND = pygame.image.load("AnimatedStreet.png")

# FPS
FPS = 60
timer = pygame.time.Clock()

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
inform1 = pygame.font.SysFont("Verdana", 20).render("Press any key to play again", True, BLACK)
inform2 = pygame.font.SysFont("Verdana", 20).render("Press SPACEBAR to exit", True, BLACK)
inform3 = pygame.font.SysFont("Verdana", 30).render(f"Coins collected {menuScore}", True, BLUE)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.surf = pygame.Surface(self.image.get_size())

        center = (WIDTH // 2, HEIGHT - self.image.get_height() // 2)
        self.rect = self.surf.get_rect(center=center)

        self.speed = 300
 
    def move(self):
        pixels_per_frame = self.speed // FPS
        pressed_keys = pygame.key.get_pressed()

        # if self.rect.top > 0:
        #     if pressed_keys[pygame.K_UP]:
        #         self.rect.move_ip(0, -pixels_per_frame)
        # if self.rect.bottom < HEIGHT:
        #     if pressed_keys[pygame.K_DOWN]:
        #         self.rect.move_ip(0, pixels_per_frame)
         
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-pixels_per_frame, 0)
        if self.rect.right < WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(pixels_per_frame, 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Coin.png")
        self.width, self.height = self.image.get_size()
        self.surf = pygame.Surface(self.image.get_size())

        center = (random.randint(self.width // 2, WIDTH - self.width // 2), 
                  -self.height // 2)
        self.rect = self.surf.get_rect(center=center)
        self.speed = 300

    def move(self):
        pixels_per_frame = self.speed // FPS
        self.rect.move_ip(0, pixels_per_frame)
        if self.rect.top > HEIGHT:
            center = (random.randint(self.width // 2, WIDTH - self.width // 2), 
                    -self.height // 2)
            self.rect.center = center

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.width, self.height = self.image.get_size()
        self.surf = pygame.Surface(self.image.get_size())

        center = (random.randint(self.width // 2, WIDTH - self.width // 2), 
                  -self.height // 2)
        self.rect = self.surf.get_rect(center=center)

        self.speed = random.randint(60,300)

    def move(self):
        global score
        pixels_per_frame1 = self.speed // FPS
        

        self.rect.move_ip(0,pixels_per_frame1)
        if self.rect.top > HEIGHT:
            score += 1
            self.speed = random.randint(60,300)
            center = (random.randint(self.width // 2, WIDTH - self.width // 2), 
                    -self.height // 2)
            self.rect.center = center

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Creating our own event
#INC_SPEED = pygame.USEREVENT + 1
#pygame.time.set_timer(INC_SPEED, 1000)

game_done = False
while not game_done:
    # Creating sprites
    enemy1 = Enemy()
    player1 = Player()
    coin1 = Coin()
    #Creating Sprites Groups
    enemies = pygame.sprite.Group()
    enemies.add(enemy1)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player1)
    all_sprites.add(enemy1)
    all_sprites.add(coin1)
    coins = pygame.sprite.Group()
    coins.add(coin1)
    coin_cnt = 0
    score = 0
    done = False
    while not done:
        timer.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                game_done = True
            # if event.type == INC_SPEED:
            #     for sprite in all_sprites:
            #         sprite.speed += 100
        
        if pygame.sprite.spritecollideany(player1,coins ):
            pygame.mixer.Sound('mcs.mp3').play()
            for c in coins:
                c.kill()
            coin1.kill()
            new_coin = Coin()
            all_sprites.add(new_coin) 
            coins.add(new_coin)
            coin_cnt+=1

        if pygame.sprite.spritecollideany(player1, enemies):
            pygame.mixer.Sound('crash.wav').play()
            DISPLAYSURF.fill(RED)
            menuScore = coin_cnt
            
            inform3 = pygame.font.SysFont("Verdana", 30).render(f"Coins collected {menuScore}", True, BLUE)
            
            txt_rect = game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2-100))
            DISPLAYSURF.blit(game_over, txt_rect)
            txt1info = inform1.get_rect(center=(WIDTH // 2, HEIGHT // 2+20))
            txt2info = inform2.get_rect(center=(WIDTH // 2, HEIGHT // 2+70)) 
            txt3info = inform3.get_rect(center=(WIDTH // 2, HEIGHT // 2-200))

            DISPLAYSURF.blit(inform3, txt3info)
            DISPLAYSURF.blit(inform1, txt1info)
            DISPLAYSURF.blit(inform2, txt2info)
            pygame.display.flip()
            for sprite in all_sprites:
                sprite.kill()
            choosen = False
            while not choosen:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_done = True
                        choosen = True
                    if event.type == pygame.KEYDOWN:
                        choosen = True
                        if event.key == pygame.K_SPACE:
                            game_done = True
            done = True

        DISPLAYSURF.blit(BACKGROUND, (0, 0))

        
        score_coin = font_small.render(str(coin_cnt), True, BLACK)
        DISPLAYSURF.blit(score_coin, (360,10))

        scores = font_small.render(str(score), True, BLACK)
        DISPLAYSURF.blit(scores, (10, 10))
        pygame.draw.circle(DISPLAYSURF, (255,255,0), (371,50), 10)
        pygame.draw.line(DISPLAYSURF,WHITE,(370,42), (370,57),4)
        for sprite in all_sprites:
            sprite.move()
            sprite.draw(DISPLAYSURF)

        pygame.display.flip()

pygame.quit()