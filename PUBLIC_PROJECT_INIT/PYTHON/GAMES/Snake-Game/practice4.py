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

main_image = pygame.image.load("inicio1.png")
gamepaused = pygame.image.load("gamepaused.png")

class Snake():
    """Creacion del Snake."""

    def __init__(self):
        self.velocity = 20
        self.length_cola = 0
        self.snake_headbody = [[220, 200]]
        self.current_movements = random.choice(["right", "left", "up", "down"])
        self.wrong_movements = {
        "right": ["left"],
        "left": ["right"],
        "up": ["down"],
        "down": ["up"]
        }
        self.best_score = 0
        self.current_score = 0

    def draw_snake(self, screen):
        for index, body in enumerate(self.snake_headbody):
            if index == 0:
                pygame.draw.rect(screen, YELLOW, [body[0], body[1], 20, 20], 5)
                continue
            pygame.draw.rect(screen, PURPLE, [body[0], body[1], 20, 20], 5)

        self.check_error()

    def possbile_moves_snake(self, screen):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if self.check_valid_movement(pygame.key.name(event.key)):
                        continue
                    self.current_movements = "up"
                if event.key == pygame.K_DOWN:
                    if self.check_valid_movement(pygame.key.name(event.key)):
                        continue
                    self.current_movements = "down"
                if event.key == pygame.K_RIGHT:
                    if self.check_valid_movement(pygame.key.name(event.key)):
                        continue
                    self.current_movements = "right"
                if event.key == pygame.K_LEFT:
                    if self.check_valid_movement(pygame.key.name(event.key)):
                        continue
                    self.current_movements = "left"
                if event.key == pygame.K_SPACE:
                    pause_game(screen)


        self.snake_movements(screen)

    def snake_movements(self, screen):
        if self.current_movements == "right":
            move_right = self.snake_headbody[0][0] + self.velocity
            x = self.check_bounds(move_right, "max_limit")
            self.update_snake(x, "X", screen)
        if self.current_movements == "left":
            move_left = self.snake_headbody[0][0] - self.velocity
            x1 = self.check_bounds(move_left, "min_limit")
            self.update_snake(x1, "X", screen)
        if self.current_movements == "up":
            move_up = self.snake_headbody[0][1] - self.velocity
            y = self.check_bounds(move_up, "min_limit")
            self.update_snake(y, "Y", screen)
        if self.current_movements == "down":
            move_down = self.snake_headbody[0][1] + self.velocity
            y1 = self.check_bounds(move_down, "max_limit")
            self.update_snake(y1, "Y", screen)

    def update_snake(self, value, key, screen):
        if key == "X":
            self.snake_headbody.insert(0, [value, self.snake_headbody[0][1]])
            self.snake_headbody.pop()
            self.draw_snake(screen)
        else:
            self.snake_headbody.insert(0, [self.snake_headbody[0][0], value])
            self.snake_headbody.pop()
            self.draw_snake(screen)

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

    def check_valid_movement(self, next_mov):
        if next_mov in self.wrong_movements[self.current_movements]:
            return True

    def get_snake_head(self):
        return self.snake_headbody[0]

    def grow_snake(self, value, screen):
        self.snake_headbody.insert(0, list(value))
        self.draw_snake(screen)

    def check_error(self):
        if self.get_snake_head() in self.snake_headbody[2:]:
            self.reset()

    def reset(self):
        message(self.length_cola)
        self.snake_headbody = [[220, 200]]
        self.current_movements = random.choice(["right", "left", "up", "down"])

        if self.length_cola > self.current_score:
            self.current_score = self.length_cola
            self.best_score = self.length_cola
        self.length_cola = 0


def message(score):
    wn = tk.Tk()
    wn.withdraw()
    mensaje = "Oh no! Has chocado!"
    messagebox.showwarning(message=f"{mensaje} Tu score es: {score}")
    try:
        wn.destroy()
    except Exception as e:
        raise

    time.sleep(1)


class Food():
    """Creacion del Food."""

    def __init__(self):
        self.food_position = (0, 0)
        self.food_random_position()

    def food_random_position(self):
        self.food_position = (random.randrange(0, 680, 20), random.randrange(0, 680, 20))

    def draw_food(self, screen):
        pygame.draw.circle(screen, RED, (self.food_position[0]+10, self.food_position[1]+10), 10, 5)

def check_food(snake, food, screen):
    if tuple(snake.get_snake_head()) == food.food_position:
        snake.grow_snake(food.food_position, screen)
        food.food_random_position()
        food.draw_food(screen)

        snake.length_cola += 1

        if snake.length_cola > snake.best_score:
            snake.best_score = snake.length_cola


class Block():
    """Creacion del Block."""

    def __init__(self):
        self.block_position = (0, 0)
        self.block_random_position()

    def block_random_position(self):
        self.block_position = [(random.randrange(0, 680, 20), random.randrange(0, 680, 20)) for i in range(5)]

    def draw_block(self, screen):
        for index, bloque in enumerate(self.block_position):
            pygame.draw.rect(screen, BLUE, [bloque[0], bloque[1], 20, 20], 5)

def check_block(snake, block):
    if tuple(snake.get_snake_head()) in block.block_position:
        block.block_random_position()
        snake.reset()

def draw_grid(screen):
    screen.fill(GREEN_LIME)
    x_line = 0
    y_line = 0
    for point in range(WIDTH):
        x_line += size_grid
        y_line += size_grid
        pygame.draw.line(screen, BLACK, (x_line, 0), (x_line, HEIGHT))
        pygame.draw.line(screen, BLACK, (0, y_line), (WIDTH, y_line))

def start_menu(start, screen):
    screen.blit(main_image, (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return False
    return True

def pause_game(screen):
    # paused = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    return False
                elif event.type == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        screen.blit(gamepaused, (0, 0))
        pygame.display.update()

def main():
    pygame.init()
    screen = pygame.display.set_mode(size_screen)
    pygame.display.set_caption("SNAKE GAME NOOB")
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()
    block = Block()
    game_score_font = pygame.font.SysFont("TerminessTTF Nerd Font", 28)
    start = True
    while True:
        clock.tick(10)
        snake.possbile_moves_snake(screen)
        draw_grid(screen)
        food.draw_food(screen)
        block.draw_block(screen)
        snake.draw_snake(screen)
        check_food(snake, food, screen)
        check_block(snake, block)

        score_text = game_score_font.render(f"Score: {snake.length_cola}", True, WHITE)
        screen.blit(score_text, (5, 3))
        score_text = game_score_font.render(f"Best Score: {snake.best_score}", True, WHITE)
        screen.blit(score_text, (5, 23))

        while True:
            if food.food_position in block.block_position:
                food.food_random_position()
            break
        while start:
            start = start_menu(start, screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()
