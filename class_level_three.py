import pygame
from class_level import Level
from class_boss import Boss
from functions import *


class LevelThree(Level):
    def __init__(self, screen):

        background = pygame.image.load("assets/fondos/fondo_4.png").convert_alpha()

        player_list3 = []
        player_list3.append(pygame.image.load("assets/nave_5.png"))
        player_list3.append(pygame.image.load("assets/nave_6.png"))

        self.boss_list = []
        self.boss_list.append(pygame.image.load("assets/enemy_boss.png"))
        self.boss_list.append(pygame.image.load("assets/enemy_boss_damaged.png"))

        enemy_bullet_list = []
        enemy_bullet_list.append(pygame.image.load("assets/bullets/charged1.png"))
        enemy_bullet_list.append(pygame.image.load("assets/bullets/charged2.png"))
        enemy_bullet_list.append(pygame.image.load("assets/bullets/charged3.png"))
        enemy_bullet_list.append(pygame.image.load("assets/bullets/charged4.png"))
        enemy_bullet_list.append(pygame.image.load("assets/bullets/charged5.png"))
        enemy_bullet_list.append(pygame.image.load("assets/bullets/charged6.png"))
        
        self.boss_bullets_animation = show_animation(4, "assets/bullets/shoot", "png")
        self.boss_list_group = pygame.sprite.Group()
        self.boss_bullets = pygame.sprite.Group()
        self.parable_bullets = pygame.sprite.Group()
        self.time_since_last_shot = 0
        self.last_time = pygame.time.get_ticks()
        self.current_time = pygame.time.get_ticks()
        self.last_shoot_time = 0
        self.shoot_interval = 1500
        self.boss_shield = 100


        self.level_completed = False

        self.story = "historia_3"


        
        
        super().__init__(screen, background, player_list3)

        self.enemy_boss = Boss(self.all_sprites,enemy_bullet_list, self.boss_bullets_animation, self.parable_bullets, self.boss_list)


        
        self.spawn_boss()
        self.spawn_initial_enemies()

    
    def spawn_boss(self):
        self.enemy_boss = Boss(self.all_sprites, self.boss_bullets_animation,self.boss_bullets, self.parable_bullets, self.boss_list)
        self.boss_list_group.add(self.enemy_boss)
        self.all_sprites.add(self.enemy_boss)
    
    
    def game_screen_menu(self):
        show_screen_paused(create_game_pause, self.screen, self.background)

    def shoot_delay(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shoot_time >= self.shoot_interval:
            if self.boss_shield > 50:
                self.enemy_boss.triple_shoot()
            elif self.boss_shield <= 50:
                self.enemy_boss.parable_shoot()
                
            self.last_shoot_time = current_time
        
        
    def handle_collisions(self):
        super().handle_collisions()
        hits_in_boss = pygame.sprite.groupcollide(self.boss_list_group, self.bullets, False, True)
        
        for hits in hits_in_boss:
            self.update_score(10)
            self.boss_shield -=50
            self.enemy_boss.boss_is_animating = True
            if self.boss_shield == 0:
                self.level_completed = True
                
        
        hits_in_player = pygame.sprite.spritecollide(self.player, self.boss_bullets,True)
        for hit in hits_in_player:
            self.damage_sound.play()
            self.player.is_animating = True
            self.player_shield -= 25
            if self.player_shield <= 0:
                self.open_menu = True

        hits_in_player_2 = pygame.sprite.spritecollide(self.player, self.parable_bullets,True)
        for hit in hits_in_player_2:
            self.damage_sound.play()
            self.player.is_animating = True
            self.player_shield -= 25
            if self.player_shield <= 0:
                self.open_menu = True
    def update(self, events_list):

        draw_shield_bar(self.screen, 795, 5, self.boss_shield, ROJO)
        self.boss_bullets.draw(self.screen)
        self.shoot_delay()
        pygame.display.flip()
        super().update(events_list)
    


            
