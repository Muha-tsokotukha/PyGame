import pygame
import sys
import random
import json
from First import _1lvl
from Second import _2lvl
from Third import _3lvl
from TwoPlayer import _2players
from LoadFirst import Saved_1lvl
from LoadSecond import Saved_2lvl
from LoadThird import Saved_3lvl



def lvl_Choosing(scr):
    bg = pygame.image.load('ChooseLVL.png')
    #132.186
    while True:
        scr.blit(bg, (0,0))
        pygame.display.update()
        x,y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (x in range(132, 186)) and (y in range(153, 203)):
                    _1lvl()
                if (x in range(210, 270)) and (y in range(153, 203)):
                    _2lvl()
                if (x in range(293, 350)) and (y in range(153, 203)):
                    _3lvl()
                

                                
def _menu(scr):
    bg = pygame.image.load('menu.png')
    #150, 134
    while True:
        scr.blit(bg, (0,0))
        x,y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (x in range(150, 320)) and (y in range(134, 174)):
                    try:
                        with open('SavedSnake.txt') as f:
                            data = json.load(f)
                            level = data[0]
                            Savescr = data[1]
                            Savepos = data[2]
                            if level == 1:
                                Saved_1lvl(Savescr, Savepos)
                            elif level == 2:
                                Saved_2lvl(Savescr, Savepos)
                            else:
                                Saved_3lvl(Savescr, Savepos)
                    except:
                        print('No saved data')
                    #loading continue
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (x in range(150,318) ) and (y in range(75,118) ):
                    _2players()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (x in range(150, 320)) and (y in range(189, 228)):
                    lvl_Choosing(scr)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (x in range(150, 320)) and (y in range(242, 280)):
                    pygame.quit()
                    sys.exit()
            
            

        pygame.display.update()