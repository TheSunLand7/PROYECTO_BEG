import pygame, sys, random, time
import tkinter as tk
from tkinter import messagebox

# Colores a usar en el juego
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GREEN_LIME = (0, 204, 0)
AZURE = (0, 127, 255)
ORANGE = (255, 103, 0)
BROWN = (139, 69, 19)
SILVER = (201, 192, 187)
PURPLE = (138, 43, 226)
YELLOW = (255, 255, 0)

WIDTH = 700
HEIGHT = 700
size_screen = (WIDTH, HEIGHT)
size_grid = 20
main_image = pygame.image.load("inicio1.png")
pause_image = pygame.image.load("gamepaused.png")

# Para crear a la serpiente
class Snake():
    """docstring for Snake."""

    def __init__(self):
        self.velocity = 20
        self.length = 1  # Cabeza de la serpiente
        self.snake_body = [[220, 200]]
        # Almacena los movimientos actuales. Empieza con un aleatorio
        self.actual_movements = random.choice(["right", "left", "up", "down"])
        self.wrong_movements = {
        "right": ["left"],
        "left": ["right"],
        "up": ["down"],
        "down": ["up"]
        }  # Para verificar los movimientos permitidos y los que no.
        # Si la serpiente va hacia la derecha no puede volver hacia la izquierda
        self.best_score = 1  # Almacena la puntuación máxima
        self.act_score = 1  # Almacena la puntuacion actual

    def move_snake(self, screen):
        """Controla los eventos que ocurre en la serpiente"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Cuando se presiona un teclado
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    # Si la serpiente se mueve a una dirección y yo quiero moverla
                    # a una contraria, la serpiente debe continuar moviendose
                    # en su dirección original
                    if self.check_valid_movement(pygame.key.name(event.key)):
                        continue
                    self.actual_movements = "left"
                if event.key == pygame.K_RIGHT:
                    if self.check_valid_movement(pygame.key.name(event.key)):
                        continue
                    self.actual_movements = "right"
                if event.key == pygame.K_UP:
                    if self.check_valid_movement(pygame.key.name(event.key)):
                        continue
                    self.actual_movements = "up"
                if event.key == pygame.K_DOWN:
                    if self.check_valid_movement(pygame.key.name(event.key)):
                        continue
                    self.actual_movements = "down"
                if event.key == pygame.K_SPACE:
                    pause_game(screen)

        self.snake_movements(screen)

    def snake_movements(self, screen):
        """Para que la serpiente se siga moviendo cuando no se presiona otra tecla"""
        if self.actual_movements == "right":
            # snake_body[0][0] representa la posici+on x
            temp = self.snake_body[0][0] + self.velocity  # El valor de las x's se suman a la velocidad
            x = self.check_bounds(temp, "max_limit")  # Cuando el snake llegue al limite
            self.update_snake(x,  "X", screen)  # Como me muevo horizontalmente le colocamos "X"
        if self.actual_movements == "left":
            # snake_body[0][0] representa la posici+on x
            temp = self.snake_body[0][0] - self.velocity  # El valor de las x's se suman a la velocidad
            x = self.check_bounds(temp, "min_limit")  # Cuando el snake llegue al limite
            self.update_snake(x, "X", screen)  # Como me muevo horizontalmente le colocamos "X"
        if self.actual_movements == "up":
            # snake_body[0][1] representa la posici+on y
            temp = self.snake_body[0][1] - self.velocity  # El valor de las y's se suman a la velocidad
            y = self.check_bounds(temp, "min_limit")  # Cuando el snake llegue al limite
            self.update_snake(y, "Y", screen)  # Como me muevo verticalmente le colocamos "Y"
        if self.actual_movements == "down":
            # snake_body[0][1] representa la posici+on y
            temp = self.snake_body[0][1] + self.velocity  # El valor de las y's se suman a la velocidad
            y = self.check_bounds(temp, "max_limit")  # Cuando el snake llegue al limite
            self.update_snake(y, "Y", screen)  # Como me muevo verticalmente le colocamos "Y"

    # Cada vez que se crea una variable temporal(movimientos de la serpiente),
    # llamamos la función "update_snake" y le pasamos el valor de "temp"
    def update_snake(self, value, key, screen):
        """Para que la serpiente se vaya actualizando"""
        if key == "X":
            # Se modifica el valor de "x" pero no de "y"
            self.snake_body.insert(0, [value, self.snake_body[0][1]])
            self.snake_body.pop()  # Para eliminar el rastro de la snake
            self.draw_snake(screen)
        else:
            # Se modifica el valor de "y" pero no de "x"
            self.snake_body.insert(0, [self.snake_body[0][0], value])
            self.snake_body.pop()  # Para eliminar el restro de la snake
            self.draw_snake(screen)

    def draw_snake(self, screen):
        """Para dibujar a la sepiente"""
        # Para recorrer el cuerpo de la serpiente
        for idx, body in enumerate(self.snake_body):  # idx Itera el indice en el cual vamos
            if idx == 0:  # Si nos encontramos en la cabeza de la serpiente
                pygame.draw.rect(screen, YELLOW, [body[0], body[1], 20, 20])
                continue
            pygame.draw.rect(screen, PURPLE, [body[0], body[1], 20, 20])



    def check_valid_movement(self, next_mov):
        """Para verificar movimientos válidos"""
        if next_mov in self.wrong_movements[self.actual_movements]:
            return True

    def check_bounds(self, value_to_check, limit):
        """Para que la serpiente retorne por el lado opuesto una vez que haya
        chocado con el borde"""
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

    def get_snake_head(self):
        """Retorna la posicion de la cabeza de la serpiente"""
        return self.snake_body[0]

    def grow_snake(self, value, screen):
        self.snake_body.insert(0, list(value))
        self.draw_snake(screen)

    def check_error(self, screen):
        """Resetear la serpiente cuando choque con su cuerpo"""
        #  Como la cabeza no puede chocar con la primera cola, se coloca
        #  a partir de la segunda cola "self.snake_body[2:]"
        if self.get_snake_head() in self.snake_body[2:]:
            self.reset()  # Resetea la serpiente y queda solo su cabeza

    def reset(self):
        message(self.length)
        self.snake_body = [[220, 200]]  # Solo la cabeza queda
        self.actual_movements = random.choice(["right", "left", "up", "down"])

        # Para que se guarde la puntuacion mas alta obtenida
        if self.length > self.act_score:
            self.act_score = self.length
            self.best_score = self.length
        self.length = 1

# Fuera de la clase Snake por que es una ventana aparte de tkinter
def message(score):
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror(message=f"Oh no! Has chocado! Tu score es: {score}",
    title="You've lost!")
    try:
        root.destroy()
    except Exception as e:
        pass
    time.sleep(1)

class Food():
    """Crear de manera aleatoria la comida"""
    def __init__(self):
        self.food_position = (0, 0)  # posicion de la comida
        self.random_position()

    def random_position(self):
        self.food_position = (random.randrange(0, 680, 20), random.randrange(0, 680, 20))

    def draw_food(self, screen):
        pygame.draw.rect(screen, RED, [self.food_position[0], self.food_position[1], 20, 20])

class Block():
    """Para crear los bloques de la serpiente"""

    def __init__(self):
        self.block_position = (0, 0)
        self.random_position()

    def random_position(self):
        """Valores aleatorios para los bloques"""
        self.block_position = [(random.randrange(0, 680, 20), random.randrange(0, 680, 20)) for i in range(5)]  # Una lista porque quiero crear 5 bloques

    def draw_block(self, screen):
        for i, value in enumerate(self.block_position):
            pygame.draw.rect(screen, BLACK, [value[0], value[1], 20, 20])


def check_food(snake, food, screen):
    if tuple(snake.get_snake_head()) == food.food_position:
        snake.grow_snake(food.food_position, screen)
        food.random_position()
        food.draw_food(screen)
        snake.length += 1

        if snake.length > snake.best_score:
            snake.best_score += 1

def check_block(snake, block):
    if tuple(snake.get_snake_head()) in block.block_position:
        block.random_position()
        snake.reset()

def draw_grid(screen):
    screen.fill(GREEN_LIME)
    x = 0
    y = 0
    # Para crear las cuadrículas en la ventana
    for point in range(WIDTH):
        x += size_grid
        y += size_grid
        pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT))  # Líneas verticales
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y))  # Líneas horizontales

def start_menu(start, screen):
    """Antes de iniciar el juego, presionar la tecla enter"""
    # Primero se coloca la imagen antes de iniciar el juego
    screen.blit(main_image, (0, 0))  # Para cargar la imagen
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
    """Pausar el juego y elegir si continuar o no"""
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        #  Primero se presiona la tecla de pausa y luego se coloca la imagen
        screen.blit(pause_image, (0, 0))
        pygame.display.update()

def main():
    pygame.init()
    screen = pygame.display.set_mode(size_screen)
    pygame.display.set_caption("Game Snake")  # Título de la ventana
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()  # Para que la comida se vea
    block = Block()
    start = True
    #-------------TEXTO PARA LA PUNTUACION DEL JUEGO------------->
    game_font = pygame.font.SysFont("TerminessTTF Nerd Font", 28)  # Fuente del texto a mostrar
    #-------------TEXTO PARA LA PUNTUACION DEL JUEGO------------->

    while True:
        clock.tick(11)
        draw_grid(screen)  # Llamar a la funcion para que la ejecute
        snake.move_snake(screen)  # Para que escuche el teclado
        check_block(snake, block)
        while start:
            start = start_menu(start, screen)

        check_food(snake, food, screen)
        #-------------TEXTO PARA LA PUNTUACION DEL JUEGO------------->

        # El True significa "anti-aliasing", sirve para suavizar los bordes. Darle mayor realismo
        score_text = game_font.render(f"Score: {snake.length}", True, WHITE)  # Lo que va a salir en la ventana
        screen.blit(score_text, (5, 3))  # Para colocar el texto en la ventana
        best_score_text = game_font.render(f"Best Score: {snake.best_score}", True, WHITE)  # Lo que va a salir en la ventana
        screen.blit(best_score_text, (5, 23))  # Para colocar el texto en la ventana

        #-------------TEXTO PARA LA PUNTUACION DEL JUEGO------------->
        block.draw_block(screen)

        #-------------COMIDA Y BLOQUE NO COINCIDEN------------->
        while True:
            if food.food_position in block.block_position:
                food.random_position()

            break
        #-------------COMIDA Y BLOQUE NO COINCIDEN------------->
        food.draw_food(screen)
        pygame.display.update()  # Para actualizar la pantalla al igual que flip()
        # pygame.display.flip()
main()
