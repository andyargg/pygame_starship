from class_menu import Menu
from class_story_teller import StoryTeller
from class_button import Button
from class_widget import Widget
from class_label import Label
import pygame
import json

class StoryMenu(Menu):
    def __init__(self, screen, story):
        waru_list = []
        waru_list.append(pygame.image.load("assets/narrator/waru_1.png"))
        waru_list.append(pygame.image.load("assets/narrator/waru_2.png"))
        waru_list.append(pygame.image.load("assets/narrator/waru_3.png"))
        waru_list.append(pygame.image.load("assets/narrator/waru_4.png"))
        waru_list.append(pygame.image.load("assets/narrator/waru_5.png"))
        waru_list.append(pygame.image.load("assets/narrator/waru_6.png"))
        waru_list.append(pygame.image.load("assets/narrator/waru_7.png"))
        waru_list.append(pygame.image.load("assets/narrator/waru_8.png"))
        waru_list.append(pygame.image.load("assets/narrator/waru_9.png"))
        waru_list.append(pygame.image.load("assets/narrator/waru_10.png"))
        waru_list.append(pygame.image.load("assets/narrator/waru_11.png"))
        waru_list.append(pygame.image.load("assets/narrator/waru_12.png"))
        waru_list.append(pygame.image.load("assets/narrator/waru_13.png"))
        waru_list.append(pygame.image.load("assets/narrator/waru_14.png"))

        self.story_index = 0

        self.story = self.read_story_file("story.json", story)
        story_teller = StoryTeller(700,200, waru_list)
        background = Widget(0,0, "assets/fondos/fondo_story.png")
        self.label_story = Label(50,500, "assets/fondos/text_label.png", self.story[self.story_index ], 20, 20)
        button_next = Button(700,30,"assets/fondos/flecha_derecha.png", self.next_chat)
        button_back = Button(20,30,"assets/fondos/flecha_izquierda.png", self.back_chat)
        
        

        widget_list = [background, story_teller, self.label_story, button_next, button_back]# next_button, back_button ]
       
        
        super().__init__(widget_list, screen)

    def next_chat(self):
        self.story_index += 1
        if self.story_index >= len(self.story):
            dialogue = "story completed"
            self.set_dialogue(dialogue)
        else:
            self.label_story.text = self.story[self.story_index]
            
    def back_chat(self):
        if self.story_index > 0:
            self.story_index -= 1
            self.label_story.text = self.story[self.story_index]

    def read_story_file(self, file_path, story):
        with open(file_path, "r") as file:
            story_dict = json.load(file)
        return story_dict[story]
            
            
            
            

            

                            
    
















       