# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 12:15:58 2021

@author: josue
"""

import pygame
import sys

pygame.init()

size_screen = (900, 600)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
AZURE = (0, 127, 255)
ORANGE = (255, 103, 0)
BROWN = (139, 69, 19)
SILVER = (201, 192, 187)

windows = pygame.display.set_mode(size_screen)

while True:
    for event in pygame.event.get():
        # print(event)  # Para imprimir los eventos en la consola
        if event.type == pygame.QUIT:
            sys.exit()

    windows.fill(SILVER)  # Por defecto viene en negro
    """
    # Creando un muñeco de nieve
    pygame.draw.circle(windows, WHITE, (200, 210), 40)  # Cabeza 
    pygame.draw.circle(windows, WHITE, (200, 300), 55)  # Pecho
    pygame.draw.circle(windows, WHITE, (200, 410), 65)  # Inferior

    pygame.draw.line(windows, BLACK, (70, 220), (160, 270), 8)  # brazo izq. principal
    pygame.draw.line(windows, BLACK, (92, 183), (117, 246), 8)  # brazo izq. arriba
    pygame.draw.line(windows, BLACK, (65, 265), (117, 246), 8)  # brazo izq. abajo

    pygame.draw.line(windows, BLACK, (237, 269), (322, 216), 8)  # Brazo der. principal 
    pygame.draw.line(windows, BLACK, (286, 237), (298, 190), 8)  # Brazo der. arriba
    pygame.draw.line(windows, BLACK, (286, 237), (326, 247), 8)  #Brazo der. abajo

    pygame.draw.circle(windows, BLACK, (182, 195), 8, 5)  # Ojo izquierdo
    pygame.draw.circle(windows, BLACK, (214, 195), 8, 5)  # Ojo derecho

    pygame.draw.line(windows, ORANGE, (174, 229), (198, 213), 6)  # Nariz de subida
    pygame.draw.line(windows, ORANGE, (174, 229), (200, 224), 6)  # Nariz de bajada


    pygame.draw.line(windows, RED, (139, 171), (251, 171), 8)  # Línea del sombrero

    # Sombrero rectangulo
    hat_fill = pygame.Rect(162, 108, 70, 62)
    pygame.draw.rect(windows, RED, hat_fill)

    # Botones en el cuerpo
    pygame.draw.circle(windows, BLACK, (201, 287), 8)
    pygame.draw.circle(windows, BLACK, (201, 336), 8)
    pygame.draw.circle(windows, BLACK, (201, 313), 8)

    # Piso
    floor_fill = pygame.Rect(0, 458, 1000, 40)
    pygame.draw.rect(windows, BROWN, floor_fill)
    """
    pygame.display.flip()
    