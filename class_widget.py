import pygame


class Widget:
    def __init__(self, x, y, image_path) -> None:
    
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 

    def update(self, screen, event_list):
        screen.blit(self.image, self.rect)
        
    

