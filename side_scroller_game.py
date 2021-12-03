import pygame, sys
from pygame import display
from pygame.locals import *
import random, time
from pygame import mixer
 
pygame.init()

FPS = 240
FramePerSec = pygame.time.Clock()

BLUE  = (0, 0, 255)
NOT_RED   = (25, 175, 194)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
SPEED = 5
SCORE = 0

font = pygame.font.SysFont("symbol", 30)
font_small = pygame.font.SysFont("symbol", 20)

background = pygame.image.load("road.png")

rect_of_background = background.get_rect ()
rect_of_background.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("side_scroller.png")
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH, random.randint(0,SCREEN_HEIGHT))



    def move(self):
        global SCORE
        self.rect.move_ip(-SPEED, 0)
        if (self.rect.left <= 0):
            SCORE += 1
            self.rect.right = SCREEN_HEIGHT / 2
            self.rect.center = (SCREEN_WIDTH, random.randint(0,SCREEN_HEIGHT))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Porsche.png")
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()

       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        


        if pressed_keys[K_UP] and self.rect.top >= 0:
            self.rect.move_ip(0, -10)
                
        if pressed_keys[K_DOWN] and self.rect.bottom <= SCREEN_HEIGHT:
            self.rect.move_ip(0, 10)
      
                  
player = Player()
E1 = Enemy()
E2 = Enemy()


enemies = pygame.sprite.Group()
enemies.add(E1)
enemies.add(E2)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(E1)
all_sprites.add(E2)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

DISPLAYSURF.blit(pygame.image.load("road.png"), (0, 0))

soundobj = pygame.mixer.Sound('mocha_frapp.mp3')
soundobj.play()
soundobj.set_volume(0.2)
while True:
    
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 1     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, rect_of_background)
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))

    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
        
    game_over = font.render(f"Game Over your score: {SCORE}", True, BLACK)

    if pygame.sprite.spritecollideany(player, enemies):
        soundobj1 = pygame.mixer.Sound('hit.wav')
        soundobj1.play()  
        soundobj1.set_volume(5)
        DISPLAYSURF.fill(NOT_RED)
        DISPLAYSURF.blit(game_over, (30,250))
        
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()   
        

    pygame.display.update()
    FramePerSec.tick(FPS)
