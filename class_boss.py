import pygame,random
from class_enemy import Enemy
from constantes import *
from class_boss_bullet import BossBullet
from class_boss_parabolic_bullet import BossParabolicBullet
from functions import *

class Boss(Enemy):
    def __init__(self, all_sprites, bullet_animation_list, boss_triple_bullets, parable_bullet, boss_list):
        super().__init__(all_sprites)
        self.sprites =  boss_list
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.boss_is_animating = False
        self.rect.x  = random.randrange(ANCHO_VENTANA -  self.rect.width)
        self.speedx = random.randint(-3,3)
        self.bullet_animation = bullet_animation_list #image list
        self.boss_triple_bullets = boss_triple_bullets#grupo
        self.parable_bullet = parable_bullet#grupo
        self.change_speed_timer = pygame.time.get_ticks() + random.randint(500,1000)  # Establece un temporizador inicial
        
    def animating(self):
        self.boss_is_animating = True
    
    def update(self):
        
        if self.boss_is_animating:
            self.current_sprite += 0.2
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.boss_is_animating = False
            
            self.image = self.sprites[int(self.current_sprite)]
        

        current_time = pygame.time.get_ticks()
        if current_time > self.change_speed_timer:
            self.speedx = random.randint(-5,5 )  # Cambia la velocidad aleatoriamente
            if self.rect.left == 0:
                self.speedx = random.randint(3, 7)  # Cambia la velocidad si toca el borde izquierdo
            elif self.rect.right == ANCHO_VENTANA:
                self.speedx = random.randint(-7, -4)
            self.change_speed_timer = current_time + random.randint(500, 1000)  # Establece el próximo temporizador

        self.rect.x += self.speedx
        if self.rect.right > ANCHO_VENTANA:
            self.rect.right = ANCHO_VENTANA
        if self.rect.left < 0:
            self.rect.left = 0
    
    def triple_shoot(self):

        bullet1 = BossBullet(self.rect.centerx, self.rect.bottom,  self.bullet_animation, 10)
        bullet2 = BossBullet(self.rect.centerx, self.rect.bottom,  self.bullet_animation)
        bullet3 = BossBullet(self.rect.centerx, self.rect.bottom,  self.bullet_animation, -10)
        
        self.boss_triple_bullets.add(bullet1, bullet2, bullet3)
        self.all_sprites.add(bullet1, bullet2, bullet3)
    
    def parable_shoot(self):
        
        following_bullet = BossParabolicBullet(self.rect.centerx, self.rect.bottom, show_animation(4,"assets/bullets/following_shoot","png"),4)
        following_bullet_2 = BossParabolicBullet(self.rect.centerx, self.rect.bottom, show_animation(4,"assets/bullets/following_shoot","png"),4)
        self.parable_bullet.add(following_bullet, following_bullet_2)
        self.all_sprites.add(following_bullet, following_bullet_2)
        

