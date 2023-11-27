from constantes import *
import pygame
import sys

pygame.init()


def draw_text(surface, txt, size, x, y):
    
    pygame.font.init()
    font = pygame.font.SysFont("Sans Serif",size)
    txt_surface = font.render(txt, True, BLANCO)
    txt_rect = txt_surface.get_rect()
    txt_rect.midtop = (x,y)
    surface.blit(txt_surface, txt_rect)

def draw_shield_bar(surface, x, y, percentage, color):
  
    
    fill = (percentage/100) * BAR_LENGTH
    border = pygame.Rect(x,y, BAR_LENGTH, BAR_HEIGHT)
    fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surface, color, fill)
    pygame.draw.rect(surface, BLANCO, border, 2)
    

def show_screen_paused(function, screen, background):
    function(screen, background)
        
def show_animation(iterations, base_file_name, type):
    animation = []
    for i in range(iterations):
        file = f"{base_file_name}_{i}.{type}" 
        img = pygame.image.load(file).convert_alpha()
        animation.append(img)
    return animation
        



            
