from class_widget import Widget
import pygame
from constantes import *

class Label(Widget):
    def __init__(self, x, y, image_path, text, sizex, sizey) -> None:
        super().__init__(x, y, image_path)

        self.font = pygame.font.SysFont("Calibri", sizex, sizey)
        self.text = text
        

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        self.__text = str(text)
        self.rendered_text = self.font.render(self.__text, True, BLANCO)
        self.text_rect = self.rendered_text.get_rect()
        self.text_rect.center = self.rect.center
        



    def update(self, screen, event_list):
        super().update(screen, event_list)
        screen.blit(self.rendered_text, self.text_rect)


