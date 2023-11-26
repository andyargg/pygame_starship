from class_widget import Widget
import pygame


class Button(Widget):
    def __init__(self, x, y,  image_path, on_click, parameter_1 = None) -> None:

        super().__init__(x, y,  image_path)

        self.on_click = on_click
        self.parameter_1 = parameter_1

    def update(self,screen, event_list):  
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    if self.parameter_1 != None:
                        self.on_click(self.parameter_1)
                    else:
                        self.on_click()
            