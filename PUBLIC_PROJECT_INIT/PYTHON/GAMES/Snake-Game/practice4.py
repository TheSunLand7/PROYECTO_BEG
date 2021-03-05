# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 10:57:11 2021

@author: SIR Anker
"""
import pygame, time, random, sys
import tkinter as tk
from tkinter import messagebox

# Colores a usar en la elaboracion del juego en formato RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN_LIME = (0, 204, 0)
PURPLE = (138, 43, 226)
YELLOW = (255, 255, 0)

WIDTH = 700
HEIGHT = 700

size_screen = (WIDTH, HEIGHT)
size_grid = 20  # Para las cuadrículas de la ventana

class Snake():
    """Creacion de la Snake."""

    def __init__(self):
        self.velocity = 20
        self.length = 1
        self.snake_complete = [[220, 200]]
        self.current_movements = random.choice(["right", "left", "down", "up"])
        self.wrong_movements = {
        "right": ["left"],
        "left": ["right"],
        "up": ["down"],
        "down": ["up"],
        }
        self.current_score = 0
        self.best_score = 0

    def possible_snake_moves(self, screen):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if self.check_valid_movement(pygame.key.name(event.key)):
                        continue
                    self.current_movements = "right"
                if event.key == pygame.K_LEFT:
                    if self.check_valid_movement(pygame.key.name(event.key)):
                        continue
                    self.current_movements = "left"
                if event.key == pygame.K_UP:
                    if self.check_valid_movement(pygame.key.name(event.key)):
                        continue
                    self.current_movements = "up"
                if event.key == pygame.K_DOWN:
                    if self.check_valid_movement(pygame.key.name(event.key)):
                        continue
                    self.current_movements = "down"

        self.snake_movements(screen)

    def snake_movements(self, screen):
        if self.current_movements == "right":
            move = self.snake_complete[0][0] + self.velocity
            x = self.check_bounds(move, "max_limit")
            self.update_snake(x, "X", screen)
        if self.current_movements == "left":
            move = self.snake_complete[0][0] - self.velocity
            x = self.check_bounds(move, "min_limit")
            self.update_snake(x, "X", screen)
        if self.current_movements == "up":
            move = self.snake_complete[0][1] - self.velocity
            y = self.check_bounds(move, "min_limit")
            self.update_snake(y, "Y", screen)
        if self.current_movements == "down":
            move = self.snake_complete[0][1] + self.velocity
            y = self.check_bounds(move, "max_limit")
            self.update_snake(y, "Y", screen)

    def draw_snake(self, screen):
        for index, cola in enumerate(self.snake_complete):
            if index == 0:
                pygame.draw.rect(screen, YELLOW, [cola[0], cola[1], 20, 20])
                continue
            pygame.draw.rect(screen, PURPLE, [cola[0], cola[1], 20, 20])

    def update_snake(self, value, key, screen):
        if key == "X":
            self.snake_complete.insert(0, [value, self.snake_complete[0][1]])
            self.snake_complete.pop()
            self.draw_snake(screen)
        else:
            self.snake_complete.insert(0, [self.snake_complete[0][0], value])
            self.snake_complete.pop()
            self.draw_snake(screen)

    def check_valid_movement(self, next_mov):
        if next_mov in self.wrong_movements[self.current_movements]:
            return True

    def check_bounds(self, value_to_check, limit):
        if limit == "max_limit":
            if value_to_check > 700:
                return 0
            else:
                return value_to_check
        else:
            if value_to_check < 0:
                return 700
            else:
                return value_to_check

def draw_grid(screen):
    screen.fill(GREEN_LIME)
    x = 0
    y = 0
    for point in range(WIDTH):
        x += size_grid
        y += size_grid
        pygame.draw.line(screen, BLACK, (x, 0), (y, HEIGHT))
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH, x))

def main():
    """Funcoion principal"""
    pygame.init()
    screen = pygame.display.set_mode(size_screen)
    pygame.display.set_caption("GAME OF SNAKE")
    clock = pygame.time.Clock()
    snake = Snake()

    while True:
        clock.tick(10)
        draw_grid(screen)
        snake.possible_snake_moves(screen)
        pygame.display.flip()

main()
