import pygame
from constantes import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.image = pygame.image.load("assets/disparo_normal.jpg").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.centerx = x
        self.speedy = -10
    
    def update(self):
        
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


