

from functions import *
from class_level import Level





class LevelOne(Level):
    def __init__(self,  screen):
        background = pygame.image.load("assets/fondos/fondo_2.png").convert_alpha() 
        player_list1 = []
        player_list1.append(pygame.image.load("assets/nave_0.png"))
        player_list1.append(pygame.image.load("assets/nave_1.png"))
        

      
        super().__init__(screen, background, player_list1)
        
        self.story = "historia_1"
        self.spawn_initial_enemies()
  


    def handle_collisions(self):
        super().handle_collisions()
        if self.score > 200 and self.level_completed == False:  # Si el puntaje supera 1000, guardar el puntaje
            self.level_completed = True
            self.story = "historia_2"
            


    def update_level_one(self):
        super().update_level()
        
           
           
                
            
            
        