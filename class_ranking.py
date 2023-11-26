import pygame
from class_menu import Menu
from class_button import Button
from class_widget import Widget

class Ranking(Menu):
    def __init__(self, screen) -> None:
        button_back = Button(700,600, "assets/fondos/back.png",self.set_dialogue, "Back")
        background = Widget(0,0, "assets/fondos/fondo_puntuacion.png")
        widget_list = [background, button_back]

        super().__init__(widget_list, screen)