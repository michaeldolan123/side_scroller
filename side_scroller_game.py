import pygame, sys
from pygame.locals import *
import random, time
 
pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE  = (0, 0, 255)
NOT_RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
