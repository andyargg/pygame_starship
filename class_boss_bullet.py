import pygame, random
from class_bullet import Bullet
from constantes import *


class BossBullet(Bullet):
    def __init__(self, x, y, boss_bullet_list, speedx=0) -> None:
        super().__init__(x, y)
        self.boss_bullet_list = boss_bullet_list
        self.image = self.boss_bullet_list[0]
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.speedy = random.randrange(4,7)
        self.speedx = speedx
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 250
        
    
    def update(self):
        super().update()
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.boss_bullet_list):
                self.kill()
            else:
                self.image = self.boss_bullet_list[self.frame]

        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        
    