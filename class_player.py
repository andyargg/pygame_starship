import pygame
from constantes import *
from class_bullet import *



class Player(pygame.sprite.Sprite):
    def __init__(self, all_sprites, bullets, player_list, sound) -> None:
        super().__init__()
        self.sprites = player_list
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.x = ANCHO_VENTANA // 2
        self.rect.y = ALTO_VENTANA - 100                                                
        self.speed_x = 0
        self.all_sprites = all_sprites
        self.bullets = bullets
        self.is_animating = False
        self.sound = sound

    def animating(self):
        self.is_animating = True
   
    def update(self):
        
        if self.is_animating:
            self.current_sprite += 0.2
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
            
            self.image = self.sprites[int(self.current_sprite)]

        self.speed_x = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_x = -5
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 5
        self.rect.x += self.speed_x
        
        if self.rect.right > ANCHO_VENTANA:
            self.rect.right = ANCHO_VENTANA
        if self.rect.left < 0:
            self.rect.left = 0
    
    def shoot(self):

        bullet = Bullet(self.rect.centerx, self.rect.top)
        self.all_sprites.add(bullet)
        self.bullets.add(bullet)
        self.sound.play()
        self.sound.set_volume(0.3)




        


