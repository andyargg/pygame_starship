
import pygame, random
from constantes import *
from functions import *
from class_enemy_bullet import EnemyBullet


class Enemy(pygame.sprite.Sprite):
    def __init__(self, all_sprites) -> None:
        super().__init__()
        self.image = pygame.image.load("assets/enemy.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(ANCHO_VENTANA -  self.rect.width)
        self.rect.y = random.randrange(-140, -100)
        self.speedy = random.randrange(1,10)
        self.speedx = random.randrange(-5,5)
        self.all_sprites = all_sprites
       
        

    def update(self):
        '''
        brief:
        Este metodo actualiza la posición de un Sprite y gestiona las condiciones fuera de los límites.
        '''
        
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if (self.rect.top > ALTO_VENTANA + 10) or (self.rect.left < -25)  or (self.rect.right > ANCHO_VENTANA + 22):
            self.rect.x = random.randrange(ANCHO_VENTANA - self.rect.width)
            self.rect.y = random.randrange(-100,-80)
            self.speedy = random.randrange(1,8)