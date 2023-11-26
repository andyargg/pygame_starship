       
import pygame 
from constantes import *
from class_principal_menu import PrincipalMenu


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Galaxy Renegade")
clock = pygame.time.Clock()

running = True

principal_menu = PrincipalMenu(screen)

while running:
    
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            running = False
    
        
    principal_menu.update(event_list)
    pygame.display.flip()
    clock.tick(FPS)
    

pygame.quit() 