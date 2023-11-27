import pygame
from constantes import *



class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, bullet_list):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = bullet_list
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = 3.5
        self.bullet_is_animating = False
   
    def animating(self):
        self.bullet_is_animating = True
    
    def update(self):
        
        if self.bullet_is_animating:
            self.current_sprite += 0.07
            print(f"actualizo sprite{self.current_sprite}")
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.bullet_is_animating = False
                    
            
            self.image = self.sprites[int(self.current_sprite)]
            
        self.rect.y += self.speedy
       
        if self.rect.bottom > ALTO_VENTANA:
            self.kill()

