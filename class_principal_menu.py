from class_button import Button
from class_widget import Widget
from class_menu import Menu
from constantes import *
import pygame
from class_user_menu import UserMenu
from class_ranking import Ranking



class PrincipalMenu(Menu):
    def __init__(self,  screen) -> None:
        
        
        play_button = Button(350, 300,  "assets/fondos/boton_start.png", self.open_input_menu, None)
        ranking = Button(350,360, "assets/fondos/ranking.png", self.open_ranking, None)
        quit_button = Button(350, 420,  "assets/fondos/boton_quit.png", self.delete_child, None)
        background = Widget(0,0, "assets/fondos/fondo_start.png")
        widget_list = [background, play_button, quit_button, ranking]

        music_sound_initialize = pygame.mixer.music.load("assets/sonidos/menu.mp3")
        pygame.mixer.music.play(-1)   
        pygame.mixer.music.set_volume(0.3)  
        
        super().__init__(widget_list, screen)

   
    def open_input_menu(self):
        user_menu = UserMenu(self.screen)
        self.set_child(user_menu)

    def open_ranking(self):
        ranking = Ranking(self.screen)
        self.set_child(ranking)
    

    
 