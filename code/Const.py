# C
import pygame

COLOR_ORANGE = (255, 128, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)

ENTITY_SPEED = {
    'lvl1bg0': 0,
    'lvl1bg1': 1,
    'lvl1bg2': 2,
    'lvl1bg3': 3,
    'lvl1bg4': 4,
    'lvl1bg5': 5,
    'lvl1bg6': 6,
    'Player1': 3,
    'Player2': 3,
    'Enemy1': 2,
    'Enemy2': 1
}

# h
ENTITY_HEALTH = {
    'lvl1bg0': 999,
    'lvl1bg1': 999,
    'lvl1bg2': 999,
    'lvl1bg3': 999,
    'lvl1bg4': 999,
    'lvl1bg5': 999,
    'lvl1bg6': 999,
    'Player1': 300,
    'Player2': 300,
    'Enemy1': 50,
    'Enemy2': 60,
}
# c
EVENT_ENEMY = pygame.USEREVENT + 1

# m
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - Cooperativo',
               'NEW GAME 2P - Conpetitivo',
               'SCORE',
               'EXITE')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP, 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN, 'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT, 'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT, 'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL, 'Player2': pygame.K_LCTRL}

# s
SPAWN_TIME = 4000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
