import pygame
from class_menu import Menu
from class_button import Button
from class_widget import Widget
from class_label import Label
import json

class Ranking(Menu):
    def __init__(self, screen) -> None:
        y = 260
        button_back = Button(700,600, "assets/fondos/back.png",self.set_dialogue, "Back")
        background = Widget(0,0, "assets/fondos/fondo_puntuacion.png")
        widget_list = [background, button_back]
        top_players = self.get_top(4)
        y = 205

        for player in top_players:
            time = str(player["time"])
            label_user_name = Label(100, y, "assets/fondos/label_ranking.png", player["user_name"], 50, 50)
            label_time = Label(490, y, "assets/fondos/label_ranking.png", time+ " S", 50, 50)
            widget_list.append(label_user_name)
            widget_list.append(label_time)
            y+=100
        
        super().__init__(widget_list, screen)
    
    def read_progress(self):
        try:
            with open('data.json') as file:
                data = json.load(file)
        
        except:
            data = {}
            
        return data
    
    def get_top(self, iterations):
        players_top = []
        progress = self.read_progress()

        for i in range(iterations):
            top_player = None
            
            for player in progress:
                if top_player == None or (player["time"] != None and player["time"] < top_player["time"]):
                    top_player = player
            
            if top_player != None:
                players_top.append(top_player)
                progress.remove(top_player)
        
        return players_top