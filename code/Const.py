# C
import pygame

COLOR_ORANGE = (255, 128, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)

ENTITY_SPEED = {
    'lvl1bg0': 0,
    'lvl1bg1': 1,
    'lvl1bg2': 2,
    'lvl1bg3': 3,
    'lvl1bg4': 4,
    'lvl1bg5': 5,
    'lvl1bg6': 6,
    'lvl2bg0': 0,
    'lvl2bg1': 1,
    'lvl2bg2': 2,
    'lvl2bg3': 3,
    'lvl2bg4': 4,
    'Player1': 3,
    'Player2': 3,
    'Enemy1': 1,
    'Enemy2': 1,
    'Player1Shot': 1,
    'Player2Shot': 1,
    'Enemy1Shot': 5,
    'Enemy2Shot': 2,

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
    'lvl2bg0': 999,
    'lvl2bg1': 999,
    'lvl2bg2': 999,
    'lvl2bg3': 999,
    'lvl2bg4': 999,
    'Player1': 300,
    'Player2': 300,
    'Enemy1': 50,
    'Enemy2': 60,
    'Player1Shot': 1,
    'Player2Shot': 1,
    'Enemy1Shot': 1,
    'Enemy2Shot': 1,
}

ENTITY_DAMAGE = {
    'lvl1bg0': 0,
    'lvl1bg1': 0,
    'lvl1bg2': 0,
    'lvl1bg3': 0,
    'lvl1bg4': 0,
    'lvl1bg5': 0,
    'lvl1bg6': 0,
    'lvl2bg0': 0,
    'lvl2bg1': 0,
    'lvl2bg2': 0,
    'lvl2bg3': 0,
    'lvl2bg4': 0,
    'Player1': 1,
    'Player2': 1,
    'Enemy1': 1,
    'Enemy2': 1,
    'Player1Shot': 25,
    'Player2Shot': 25,
    'Enemy1Shot': 50,
    'Enemy2Shot': 50,
}

ENTITY_SCORE = {
    'lvl1bg0': 0,
    'lvl1bg1': 0,
    'lvl1bg2': 0,
    'lvl1bg3': 0,
    'lvl1bg4': 0,
    'lvl1bg5': 0,
    'lvl1bg6': 0,
    'lvl2bg0': 0,
    'lvl2bg1': 0,
    'lvl2bg2': 0,
    'lvl2bg3': 0,
    'lvl2bg4': 0,
    'Player1': 0,
    'Player2': 0,
    'Enemy1': 100,
    'Enemy2': 125,
    'Player1Shot': 0,
    'Player2Shot': 0,
    'Enemy1Shot': 0,
    'Enemy2Shot': 0,
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 20,
    'Enemy1': 100,
    'Enemy2': 200,
}
# c
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
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

# t
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 10000
# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
