import pygame
from constantes import *
from functions import *
from class_level import Level
from class_explosion import Explosion
from class_enemy_shooter import EnemyShooter
from class_enemy_bullet import EnemyBullet
from class_enemy import Enemy


class LevelTwo(Level):
    def __init__(self, screen):

        background = pygame.image.load("assets/fondos/fondo_3.png").convert_alpha() 

        self.enemy_bullets_list = []
        self.enemy_bullets_list.append(pygame.image.load("assets/bullets/charged1.png"))
        self.enemy_bullets_list.append(pygame.image.load("assets/bullets/charged2.png"))
        self.enemy_bullets_list.append(pygame.image.load("assets/bullets/charged3.png"))
        self.enemy_bullets_list.append(pygame.image.load("assets/bullets/charged4.png"))
        self.enemy_bullets_list.append(pygame.image.load("assets/bullets/charged5.png"))
        self.enemy_bullets_list.append(pygame.image.load("assets/bullets/charged6.png"))

        player_list2 = []
        player_list2.append(pygame.image.load("assets/nave_3.png"))
        player_list2.append(pygame.image.load("assets/nave_4.png"))

        self.background = pygame.image.load("assets/fondos/fondo_3.png").convert_alpha()
        self.enemy_bullets = pygame.sprite.Group()
        self.enemy_shooter_list = pygame.sprite.Group()
        self.time_since_last_shot = 0
        self.last_time = pygame.time.get_ticks()
        self.current_time = pygame.time.get_ticks()
        self.last_shoot_time = 0
        self.shoot_interval = 3000

        self.level_2_completed = False

        self.story = "historia_2"
        
        super().__init__(screen, background, player_list2)
        self.enemy = Enemy(self.all_sprites)
        self.enemy_bullet = EnemyBullet(self.enemy.rect.centerx, self.enemy.rect.bottom, self.enemy_bullets_list)
        self.spawn_initial_enemies()
        
        
        
    def spawn_initial_enemies(self):
        for i in range(10):
            self.enemy_shooter = EnemyShooter(self.enemy_bullets, self.all_sprites, self.enemy_bullets_list)
            self.enemy_shooter_list.add(self.enemy_shooter)
            self.all_sprites.add(self.enemy_shooter)
            
            

    
    
    def handle_enemy_shooter_collisions(self):
        
        # Agregar lógica específica para enemigos shooter
        hits_in_enemy_shooters = pygame.sprite.groupcollide(self.enemy_shooter_list, self.bullets, True, True)
        for hit in hits_in_enemy_shooters:
            self.update_score(10)
            explosion = Explosion(hit.rect.center, self.explosion_animation)
            self.explosion_sound.play()
            self.explosion_sound.set_volume(0.3)
            self.all_sprites.add(explosion)
            enemy_shooter = EnemyShooter(self.enemy_bullets,self.all_sprites, self.enemy_bullets_list)
            self.all_sprites.add(enemy_shooter)
            self.enemy_shooter_list.add(enemy_shooter)
            if self.score >= 400:
                self.level_completed = True
        hits_in_players = pygame.sprite.spritecollide(self.player, self.enemy_shooter_list, True)
        for hit in hits_in_players:
            self.damage_sound.play()
            self.player.is_animating = True
            self.player_shield -= 25
            if self.player_shield <= 0:
                self.open_menu = True
        
        bullets_in_player = pygame.sprite.spritecollide(self.player,self.enemy_bullets, True)
        for hit in bullets_in_player:
            self.player.is_animating = True
            self.damage_sound.play()
            self.player_shield -= 25
            if self.player_shield <= 0:
                self.open_menu = True
        
        if self.score > 3500 and self.level_completed == False:  
            self.level_completed = True
            self.story = "historia_2"

    def shoot_delay(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shoot_time >= self.shoot_interval:
            for enemy in self.enemy_shooter_list:
                enemy.enemy_shoot()
                self.last_shoot_time = current_time
                self.enemy_bullet.bullet_is_animating = True
            
    def update(self, event_list):
        
        self.enemy_bullets.update()
        self.enemy_bullets.draw(self.screen)
        self.shoot_delay()
        self.handle_enemy_shooter_collisions()
        super().update(event_list)
        
        

