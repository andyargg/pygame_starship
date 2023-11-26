from constantes import *
import pygame
import sys

pygame.init()


def draw_text(surface, txt, size, x, y):
    '''
    Resumen:
    Esta función se encarga de dibujar texto en una superficie del juego con un tamaño de fuente, un texto y unas coordenadas específicas.

    Parámetros:
    - surface: La superficie en la que se dibujará el texto.
    - txt: El texto que se desea mostrar en la superficie.
    - size: El tamaño de fuente del texto.
    - x: La coordenada x para la posición del texto en la superficie.
    - y: La coordenada y para la posición del texto en la superficie.

    Retorno:
    La función no devuelve ningún valor explícito. Su propósito es mostrar texto en la superficie del juego.

    '''
    pygame.font.init()
    font = pygame.font.SysFont("Sans Serif",size)
    txt_surface = font.render(txt, True, BLANCO)
    txt_rect = txt_surface.get_rect()
    txt_rect.midtop = (x,y)
    surface.blit(txt_surface, txt_rect)

def draw_shield_bar(surface, x, y, percentage, color):
    '''
    Resumen:
    Esta función se utiliza para dibujar una barra de escudo en una superficie del juego, mostrando el porcentaje de llenado.

    Parámetros:
    - surface: La superficie en la que se dibujará la barra de escudo.
    - x: La coordenada x para la posición de la barra de escudo en la superficie.
    - y: La coordenada y para la posición de la barra de escudo en la superficie.
    - percentage: El porcentaje de llenado de la barra de escudo.

    Retorno:
    None

    '''
    
    fill = (percentage/100) * BAR_LENGTH
    border = pygame.Rect(x,y, BAR_LENGTH, BAR_HEIGHT)
    fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surface, color, fill)
    pygame.draw.rect(surface, BLANCO, border, 2)
    
    

def create_game_pause(screen, background):
    '''
    Resumen:
    Esta función se utiliza para crear una pantalla de pausa en el juego, mostrando un mensaje y un fondo específico.

    Parámetros:
    - screen: La superficie de la pantalla del juego en la que se mostrará la pantalla de pausa.
    - background: La imagen de fondo que se utilizará como fondo de la pantalla de pausa.

    Retorno:
    None

    '''
    screen.blit(background, [0,0])
    draw_text(screen, "Galaxy Renegade", 62, ANCHO_VENTANA//2, ALTO_VENTANA//4)
    draw_text(screen, "", 27, ANCHO_VENTANA//2, ALTO_VENTANA//2)
    draw_text(screen, "Press Key", 20, ANCHO_VENTANA//2, ALTO_VENTANA*3/4)
    pygame.display.flip()

def create_level_2(screen, background):
    '''
    Resumen:
    Esta función se utiliza para crear una pantalla que indica el inicio del nivel 2 del juego, mostrando un mensaje y un fondo específico.

    Parámetros:
    - screen: La superficie de la pantalla del juego en la que se mostrará la pantalla de inicio del nivel 2.
    - background: La imagen de fondo que se utilizará como fondo de la pantalla de inicio del nivel 2.

    Retorno:
    None
    '''
    screen.blit(background, [0,0])
    draw_text(screen, "NIVEL 2", 62, ANCHO_VENTANA//2, ALTO_VENTANA//4)
    draw_text(screen, "", 27, ANCHO_VENTANA//2, ALTO_VENTANA//2)
    draw_text(screen, "TOCA UNA TECLA PARA EMPEZAR", 20, ANCHO_VENTANA//2, ALTO_VENTANA*3/4)
    pygame.display.flip()
    
def show_screen_paused(function, screen, background):
    function(screen, background)
        
def show_animation(iterations, base_file_name, type):
    animation = []
    for i in range(iterations):
        file = f"{base_file_name}_{i}.{type}" 
        img = pygame.image.load(file).convert_alpha()
        animation.append(img)
    return animation
        



            
