from class_menu import Menu
from class_button import Button
from class_widget import Widget
from functions import *
from class_level_manager import LevelManager
from class_level_container import LevelContainer
import json



class LevelSelector(Menu):
    def __init__(self, screen, player_name) -> None:
        button_level_1 = Button(180,350,"assets/fondos/boton_1.png",self.change_level, 1)
        button_level_2 = Button(350,350,"assets/fondos/boton_2.png",self.change_level, 2)
        button_level_3 = Button(520,350,"assets/fondos/boton_3.png",self.change_level, 3)
        button_back = Button(350,500, "assets/fondos/back.png",self.set_dialogue, "Back")
        background = Widget(0,0, "assets/fondos/fondo_start.png")
        levels = Widget(340, 200, "assets/fondos/label_levels.png")

        widget_list = [background, button_level_1, button_level_2, button_level_3, levels, button_back]
        self.level_manager = LevelManager(screen)
        self.player_name = player_name
        self.read_progress()
        super().__init__(widget_list, screen)

    def change_level(self, level_int):
        level = self.level_manager.get_levels(level_int)
        level_container = LevelContainer(self.screen, level)
        self.child_form = level_container
    
    def read_progress(self):
        try:
            with open('data.json') as file:
                data = json.load(file)
       
        except:
            data = {}

        if self.player_name in data:    
            player_data = data[self.player_name]
        else:
            player_data = {
                "time": None
                }
            
        