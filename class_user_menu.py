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
                    player_name = self.player_name[:-1]
                elif event.key == pygame.K_RETURN:
                    self.save_text_to_json()
                    self.open_level_selector()
                    
        self.input_label.text = self.player_name
        super().update(event_list)
  
    def save_text_to_json(self):
        self.player_name = self.player_name.strip()

        try:
            with open("data.json", 'r', encoding='utf-8') as archivo:
                dict_list = json.load(archivo)
        except Exception as e:
            dict_list = []

        user_data = {
            'user_name': self.player_name,
            'time': None 
        }

        # Agrega el nuevo diccionario a la lista
        dict_list.append(user_data)

        try:
            with open("data.json", 'w', encoding='utf-8') as archivo:
                json.dump(dict_list, archivo, indent=2)
        except Exception as e:
            print(f"Error al actualizar el archivo JSON: {e}")
    def open_level_selector(self):
        if self.player_name != "":
            level_selector = LevelSelector(self.screen, self.player_name)
            self.set_child(level_selector)
    
   


        
    
    