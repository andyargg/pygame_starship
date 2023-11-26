
import pygame



class StoryTeller:
    def __init__(self, x, y, narrator_list) -> None:
       
        self.sprites = narrator_list
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update(self, screen, events_list):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
        self.current_sprite += 0.08
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 10
            
        
        self.image = self.sprites[int(self.current_sprite)]


    

