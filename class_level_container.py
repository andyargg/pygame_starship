import pygame
from class_menu import Menu
from class_story_menu import StoryMenu
import json







class LevelContainer(Menu):
    def __init__(self, screen, level, player_name) -> None:
        
        widget_list = []

        self.level = level
        self.player_name = player_name

        super().__init__(widget_list, screen)
    
    def save_time(self, time):
        try:
            with open("data.json", 'r', encoding='utf-8') as archivo:
                data_dict = json.load(archivo)
        except Exception as e:
            print("error")

        for element in data_dict:
            if 'user_name' in element and element['user_name'] == self.player_name:
                element['time'] = time

            
        try:
            with open("data.json", 'w', encoding='utf-8') as archivo:
                json.dump(data_dict, archivo, indent=2)
        except Exception as e:
            print(f"Error al actualizar el archivo JSON: {e}")
    
    def update(self, event_list):
        if self.level.open_menu:
            self.set_dialogue("Back")

        if self.child_form == None:
            if self.level.story != None:
                story_menu = StoryMenu(self.screen, self.level.story)
                self.set_child(story_menu)
                
            elif self.level.level_completed:
                self.save_time(self.level.update_timer())
                self.set_dialogue("Back")
                
                
            self.level.update(event_list)
        
        super().update(event_list)

    def read_dialogue(self):
        dialogo = self.get_dialogue()
        if dialogo == "story completed":
           self.delete_child()
           self.level.story = None
        else:
            super().read_dialogue()
        
            
        