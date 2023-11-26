import pygame, random
from class_bullet import Bullet
from functions import *
class BossParabolicBullet(Bullet):
    def __init__(self, x, y, bullet_following_animation, time_to_change_direction) -> None:
        super().__init__(x, y)
        self.boss_bullet_list = bullet_following_animation
        self.image = self.boss_bullet_list[0]
        self.rect = self.image.get_rect() 
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 250
        self.rect.center = (x, y)
        self.speed_x = 0
        self.speed_y = random.randrange(3,7)
        self.time = 0  
        self.time_to_change_direction = time_to_change_direction

        
                
      
    def update_animation(self):
        
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.boss_bullet_list):
                self.frame = 0
            else:
                self.image = self.boss_bullet_list[self.frame]
        
    
    def update(self):
        self.update_animation()
        
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Calcula la posición en X en función del tiempo (trayectoria parabólica)
        self.time += 0.07
        if self.time < self.time_to_change_direction:
            self.speed_x = 2 * self.time
        else:
            # Cambia la dirección de la velocidad en X
            self.speed_x = -2 * (self.time - self.time_to_change_direction)

        if self.rect.top > ALTO_VENTANA:
            self.kill()
        
       