# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 11:11:40 2021

@author: SIR Anker
"""
# Creando un juego simple con el módulo turtle
import turtle, time, random
from tkinter import messagebox

# Para que la serpiente no avance muy rápido
snooze = 0.1

# Los marcadores
current_score = 0
high_score = 0

# Ventana principal del juego
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("SNAKE GAME")
screen.tracer(0)

# Cabeza de la serpiente
snake_head = turtle.Turtle()
snake_head.shape("square")
snake_head.color("white")
snake_head.speed(0)
snake_head.up()
snake_head.goto(0, 0)
snake_head.direction = "stop"

#Manzana de la serpiente
manzana = turtle.Turtle()
manzana.shape("circle")
manzana.color("red")
manzana.speed(0)
manzana.up()
manzana.goto(0, 100)

# Funciones de movimiento
def go_up():
    snake_head.direction = "up"
def go_down():
    snake_head.direction = "down"
def go_right():
    snake_head.direction = "right"
def go_left():
    snake_head.direction = "left"

# Funciones para llamar a los movimientos
def movement():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        y += 20
        snake_head.sety(y)

    if snake_head.direction == "down":
        y1 = snake_head.ycor()
        y1 -= 20
        snake_head.sety(y1)

    if snake_head.direction == "right":
        x = snake_head.xcor()
        x += 20
        snake_head.setx(x)

    if snake_head.direction == "left":
        x1 = snake_head.xcor()
        x1 -= 20
        snake_head.setx(x1)

def main():
    global current_score
    global high_score
    #Conectar el teclado con los movimientos
    screen.listen()
    screen.onkeypress(go_up, "Up")
    screen.onkeypress(go_down, "Down")
    screen.onkeypress(go_right, "Right")
    screen.onkeypress(go_left, "Left")

    # Lista de las colas que van formando
    snake_colas = []

    # Coloca el marcador en la parte superior
    score_in_text = turtle.Turtle()
    score_in_text.color("white")
    score_in_text.speed(0)
    score_in_text.up()
    score_in_text.hideturtle()
    score_in_text.goto(0, 260)
    score_in_text.write(
    "Curent Score: 0            High Score: 0", align="center",
    font=("TerminessTTF Nerd Font", 18, "bold")
    )


    while True:
        screen.update()

        # Mover la manzana de manera aleatoria
        if snake_head.distance(manzana) < 20:
            x = random.randint(-380, 380)
            y = random.randint(-280, 280)
            manzana.goto(x, y)

            # Cuerpo de la serpiente
            snake_body = turtle.Turtle()
            snake_body.shape("square")
            snake_body.color("gray")
            snake_body.speed(0)
            snake_body.up()
            snake_colas.append(snake_body)

            # Actualizar el marcador
            current_score += 10
            if current_score > high_score:
                high_score = current_score
            score_in_text.clear()
            score_in_text.write(
            f"Curent Score: {current_score}            High Score: {high_score}", align="center",
            font=("TerminessTTF Nerd Font", 18, "bold")
            )


        # Hacer que las colas sigan a la cabeza una atras de la otra
        total_snake_colas = len(snake_colas)
        for index in range(total_snake_colas-1, 0, -1):
            x = snake_colas[index-1].xcor()
            y = snake_colas[index-1].ycor()
            snake_colas[index].goto(x, y)

        # Para hacer que la primera cola siga a la cabeza, so that las siguientes colas
        # van a seguir a la primera cola
        if total_snake_colas > 0:
            x = snake_head.xcor()
            y = snake_head.ycor()
            snake_colas[0].goto(x, y)

        # Cuando la serpiente choca con el borde
        if snake_head.xcor() > 380 or snake_head.xcor() < -380 or snake_head.ycor() > 280 or snake_head.ycor() < -280:
            message_1 = "Oh no! Has chocado con el borde!"
            messagebox.showwarning(message=f"{message_1} Tu score es: {current_score}\n El Score más alto es: {high_score}!", title="Aviso")
            time.sleep(1)
            snake_head.goto(0, 0)
            snake_head.direction = "stop"

            for cola in snake_colas:
                cola.goto(1000, 1000)
            snake_colas.clear()

            current_score = 0
            score_in_text.clear()
            score_in_text.write(
            f"Curent Score: {current_score}            High Score: {high_score}", align="center",
            font=("TerminessTTF Nerd Font", 18, "bold")
            )

        movement()
        
        for cola in snake_colas:
            if cola.distance(snake_head) < 20:
                message_2 = "Oh no! Has chocado con tu cola!"
                messagebox.showwarning(message=f"{message_2} Tu score es: {current_score}\n El Score más alto es: {high_score}!", title="Aviso")
                time.sleep(1)
                snake_head.goto(0, 0)
                snake_head.direction = "stop"

                for cola in snake_colas:
                    cola.goto(1000, 1000)
                snake_colas.clear()

                current_score = 0
                score_in_text.clear()
                score_in_text.write(
                f"Curent Score: {current_score}            High Score: {high_score}", align="center",
                font=("TerminessTTF Nerd Font", 18, "bold")
                )

        time.sleep(snooze)

main()
screen.mainloop()
