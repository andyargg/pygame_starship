import pygame
from class_enemy import Enemy
from class_enemy_bullet import EnemyBullet

class EnemyShooter(Enemy):
    def __init__(self, enemy_bullets, all_sprites, enemy_bullets_animation):
        super().__init__(all_sprites)
        self.image = pygame.image.load("assets/enemy_2.png")
        self.enemy_bullets_list = enemy_bullets#GRUPO
        self.bullets_animation = enemy_bullets_animation
        self.enemy_bullet = EnemyBullet(self.rect.centerx,self.rect.centery, self.bullets_animation)
      
    def enemy_shoot(self):
        self.enemy_bullet = EnemyBullet(self.rect.centerx, self.rect.bottom, self.bullets_animation)
        self.enemy_bullet.bullet_is_animating = True 
        self.enemy_bullets_list.add(self.enemy_bullet)
        self.all_sprites.add(self.enemy_bullet)
       
    
            
            
                
    
  