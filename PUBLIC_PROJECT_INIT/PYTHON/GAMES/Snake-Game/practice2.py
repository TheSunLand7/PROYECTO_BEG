 # -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 17:39:18 2021

@author: josue
"""

import pygame
import sys
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
AZURE = (0, 127, 255)
ORANGE = (255, 103, 0)
BROWN = (139, 69, 19)
SILVER = (201, 192, 187)


size_screen = (900, 600)
screen = pygame.display.set_mode(size_screen)
clock = pygame.time.Clock()

"""
list_coord = list()
# Guardar los puntos en una lista en pares
for point in range(100):
            x = random.randint(0, 900)
            y = random.randint(0, 600)
            list_coord.append([x, y])
"""
# Para la visibilidad del mouse en la pantalla: 0 = no visible, 1 = visible
# pygame.mouse.set_visible(0)

"""
# Coordenadas
coord_x = 10
coord_y = 10

# Velocidad
x_speed = 0
y_speed = 0
"""

while True:
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  sys.exit()
            """
            # EVENTOS TECLADO
            # Cuando se presiona un teclado
            if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_LEFT:  # Cuando se presiona tecla izq.
                        x_speed = -3
                  if event.key == pygame.K_RIGHT:  # Cuando se presiona tecla dere.
                        x_speed = 3
                  if event.key == pygame.K_UP:  # Cuando se presiona tecla up.
                        y_speed = -3
                  if event.key == pygame.K_DOWN:  # Cuando se presiona tecla down.
                        y_speed = 3

            # Cuando se deja de presionar un teclado
            if event.type == pygame.KEYUP:
                  if event.key == pygame.K_LEFT:  # Cuando se presiona tecla izq.
                        x_speed = 0
                  if event.key == pygame.K_RIGHT:  # Cuando se presiona tecla dere.
                        x_speed = 0
                  if event.key == pygame.K_UP:  # Cuando se presiona tecla up.
                        y_speed = 0
                  if event.key == pygame.K_DOWN:  # Cuando se presiona tecla down.
                        y_speed = 0
            """

      screen.fill(WHITE)
      #-------------CAIDA DE NIEVE------------>
      """
      # Numeros aleatorios en la pantalla cada 30 segundos
      for coord in list_coord:
            pygame.draw.circle(screen, RED, (coord[0], coord[1]), 2)
            coord[1] += 1
            if coord[1] > 600:
                  coord[1] = 0
      """
      #-------------CAIDA DE NIEVE------------>

      #-------------MOUSE--------------------->
      # Obtener las coordenadas del mouse mientras está en la ventana
      """
      pygame.mouse.set_visible(0)
      mouse_pos = pygame.mouse.get_pos()
      x = mouse_pos[0]
      y = mouse_pos[1]

      rect_fill = pygame.Rect(x, y, 60, 60)
      pygame.draw.rect(screen, RED, rect_fill)
      """
      #-------------MOUSE--------------------->

      #-------------TECLADO------------------->
      """
      rect_fill = pygame.Rect(coord_x, coord_y, 60, 60)
      pygame.draw.rect(screen, RED, rect_fill)
      coord_x += x_speed
      coord_y += y_speed
      """
      #-------------TECLADO------------------->

      # Para actualizar pygame (ventana)
      pygame.display.flip()
      clock.tick(60)
