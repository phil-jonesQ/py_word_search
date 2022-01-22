"""
word search Game
Phil Jones January 2021

"""

import numpy as np
import pygame
import sys
import math
import random

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)

ROW_COUNT = 6
COLUMN_COUNT = 7

PLAYER = 0
AI = 1
PLAYER2 = 1

EMPTY = 0
PLAYER_PIECE = 1
PLAYER2_PIECE = 2
AI_PIECE = 2

WINDOW_LENGTH = 4
HUD_POS = (5, 10)
HUD_POS_LARGE = (40, 10)


game_over = False
run = True
turn = PLAYER
select_level = True
select_players = True
two_players = False
ai_depth = 1

pygame.init()
SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE
size = (width, height)
RADIUS = int(SQUARESIZE/2 - 5)
screen = pygame.display.set_mode(size)
myfont = pygame.font.SysFont("monospace", 55)
myfont_small = pygame.font.SysFont("monospace", 25)


def clear_hud():
    pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
    #pygame.display.update()


def write_to_hud(message, colour, pos, size):
        if size == "small":
            label = myfont_small.render(message, 1, colour)
        else:
            label = myfont.render(message, 1, colour)
        screen.blit(label, pos)
        pygame.display.update()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        keys = pygame.key.get_pressed()
        if select_players:
            write_to_hud("SELECT PLAYERS (1) or (2)", RED, HUD_POS, "small")
            if keys[pygame.K_1]:
                select_players = False
                turn = random.randint(PLAYER, AI)
                clear_hud()
            if keys[pygame.K_2]:
                two_players = True
                select_players = False
                select_level = False
                turn = PLAYER
                clear_hud()
                pygame.display.update()
        if select_level and not select_players and not two_players:
            write_to_hud("SET AI LEVEL (E)asy (M)edium (H)ard (B)oss", RED, HUD_POS, "small")
            if keys[pygame.K_e]:
                ai_depth = 1
                select_level = False
                clear_hud()
            if keys[pygame.K_m]:
                ai_depth = 2
                select_level = False
                clear_hud()
            if keys[pygame.K_h]:
                ai_depth = 3
                select_level = False
                clear_hud()
            if keys[pygame.K_b]:
                ai_depth = 4
                select_level = False
                clear_hud()

        if keys[pygame.K_SPACE] and game_over or keys[pygame.K_r]:
            # Reset Game
            game_over = False
            piece = 0
            select_level = True
            select_players = True
            two_players = False
            clear_hud()
            pygame.display.update()


        if event.type == pygame.MOUSEBUTTONDOWN and not game_over and not select_level and not select_players:
            clear_hud()
            # Ask for Player 1 Input
            if turn == PLAYER:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
                turn += 1
                turn = turn % 2
            else: # Else it will Player 2's input
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
                turn += 1
                turn = turn % 2

    # Run If AI IS PLAYING
    if two_players == False:
        if turn == AI and not game_over and not select_level:			
            #print_board(board)
            turn += 1
            turn = turn % 2
