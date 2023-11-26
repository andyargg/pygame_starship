import pygame
from constantes import *

        
class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, explosion_list: list) -> None:
        super().__init__()
        self.explosion_list = explosion_list  
        self.image = self.explosion_list[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50  # Velocidad de la explosión

    def update(self) -> None:
        '''
    Resumen:
    Este método actualiza la animación de una explosión.

        '''
        now = pygame.time.get_ticks()
        if now - self.last_update >= self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.explosion_list):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.explosion_list[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center