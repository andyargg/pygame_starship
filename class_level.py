import pygame, sys
from constantes import *
from class_enemy import Enemy
from class_player import Player
from class_explosion import Explosion
from functions import *





class Level:
    def __init__(self, screen, background, player_list):
        self.screen = screen
        self.background = background
        self.explosion_animation = show_animation(10, "assets/explosion", "png")
        self.laser_sound = pygame.mixer.Sound("assets/sonidos/sonido_laser.mp3")
        self.explosion_sound = pygame.mixer.Sound("assets/sonidos/sonido_explosion.wav")  
        self.damage_sound = pygame.mixer.Sound("assets/sonidos/oof.mp3")
        self.all_sprites = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.player = Player(self.all_sprites, self.bullets, player_list, self.laser_sound)
        
        self.score = 0
        self.player_shield = 100

        self.all_sprites.add(self.player)
        self.all_sprites.add(self.bullets)
        
        self.open_menu = False
        self.level_completed = False
        self.story = None
 
        music_sound_initialize = pygame.mixer.music.load("assets/sonidos/street-fighter.mp3")
        pygame.mixer.music.play(-1)   
        pygame.mixer.music.set_volume(0.2)  

        
        self.seconds = 0
        self.minutes = 0


    

        


        
        
            
    def spawn_initial_enemies(self):
      
        for i in range(10):
            enemy = Enemy(self.all_sprites)
            self.all_sprites.add(enemy)
            self.enemy_list.add(enemy)
          
    def update_score(self,points):
        self.score += points
    
    def handle_events(self, event_list):
        text = " "
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = list(pygame.mouse.get_pos())
                print(posicion_click) 
                
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.KEYUP:
                
                if event.key == pygame.K_SPACE:
                    self.player.shoot()
                elif event.key == pygame.K_ESCAPE:
                    self.open_menu = True
                    
                    
            elif event.type == pygame.TEXTINPUT:
                text += event.text
                print(text)



    def handle_collisions(self):
        hits_in_enemies = pygame.sprite.groupcollide(self.enemy_list, self.bullets, True, True)
        for hit in hits_in_enemies:
            self.update_score(10)
            explosion = Explosion(hit.rect.center, self.explosion_animation)
            self.all_sprites.add(explosion)
            enemy = Enemy(self.all_sprites)
            self.all_sprites.add(enemy)
            self.enemy_list.add(enemy) 
            self.explosion_sound.play()
            self.explosion_sound.set_volume(0.3)
            

        hits_in_players = pygame.sprite.spritecollide(self.player, self.enemy_list, True)
        for hit in hits_in_players:
            self.player.is_animating = True
            self.damage_sound.play()
            self.player_shield -= 25
            if self.player_shield <= 0:
                self.open_menu = True
    
    def update_timer(self):
        self.current_time = pygame.time.get_ticks()
        self.seconds = (self.current_time/1000) 
   
        return self.seconds

        
    def update(self, event_list):
        
            self.update_timer()
            self.handle_events(event_list)    
            self.handle_collisions()
            self.bullets.update()
            self.all_sprites.update()
            self.screen.blit(self.background, (0,0))
            self.all_sprites.draw(self.screen)
            draw_text(self.screen, str(self.score), 25, ANCHO_VENTANA // 2, 10)
            draw_shield_bar(self.screen, 5, 5, self.player_shield, VERDE_AZULADO)
            
            pygame.display.flip()
            
        
            


                    
       
