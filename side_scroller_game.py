import pygame, sys
from pygame.locals import *
import random, time
 
pygame.init()

FPS = 240
FramePerSec = pygame.time.Clock()

BLUE  = (0, 0, 255)
NOT_RED   = (25, 175, 194)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 2000
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
        self.image = pygame.image.load("oil-spill.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > SCREEN_WIDTH):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (player.rect.x, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Porsche.png")
        self.rect = self.image.get_rect()

       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-20, 0)
        
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(20, 0)

        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -20)
                
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 20)


        
                  
player = Player()
E1 = Enemy()

enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(E1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    DISPLAYSURF.blit(pygame.image.load("road.png"), (0,0))

    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 1     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))

    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
        
    game_over = font.render(f"Game Over your score: {SCORE}", True, BLACK)

    if pygame.sprite.spritecollideany(player, enemies):
                   
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
