import pygame
import json
from class_menu import Menu
from class_widget import Widget
from class_label import Label
from class_button import Button
from class_level_selector import LevelSelector


class UserMenu(Menu):
    def __init__(self, screen) -> None:
        self.player_name = ""
        background = Widget(0,0, "assets/fondos/fondo_user.png")
        self.input_label = Label(70, 200, "assets/fondos/text_label.png", self.player_name, 50, 50)
        back_button = Button(360,400,"assets/fondos/back.png",self.set_dialogue, "Back")
        widget_list = [background, self.input_label, back_button]
        super().__init__(widget_list, screen)
    
    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.TEXTINPUT:
                self.player_name += event.text
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.player_name = self.player_name[:-1]
                elif event.key == pygame.K_RETURN:
                    self.open_level_selector()
        self.input_label.text = self.player_name
        super().update(event_list)

    def open_level_selector(self):
        if self.player_name != "":
            level_selector = LevelSelector(self.screen, self.player_name)
            self.set_child(level_selector)
    
   


        
    
    