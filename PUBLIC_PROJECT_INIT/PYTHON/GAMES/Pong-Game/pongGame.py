# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 16:17:03 2021

@author: josce
"""

import turtle
import winsound

# Ventana principal
wn = turtle.Screen()
wn.title("PONG GAME")
wn.setup(width=800, height=600)
wn.bgcolor("black")
wn.tracer(0)

# Scores

score_a = 0
score_b = 0

# Barra izquierda
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.color("white")
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=(5), stretch_len=(1))
paddle_a.penup()
paddle_a.goto(-350, 0)

# Barra derecha
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.color("white")
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Bola
ball = turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.shape("circle")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# Texto en pantalla
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.hideturtle()
score.penup()
score.goto(0, 260)
score.write("Payer 1:  0       Player 2:  0", align="center", font=("Consola", 14, "bold"))

# Funciones
def moveUpPaddleA():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def moveDownPaddleA():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def moveUpPaddleB():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def moveDownPaddleB():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)



def moveBall():
    global score_a
    global score_b
    
    coord_x = ball.xcor()
    coord_y = ball.ycor()
    coord_x += ball.dx
    coord_y += ball.dy
    ball.setx(coord_x)
    ball.sety(coord_y)
      
    
    if coord_x > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        score.clear()
        score.write(f"Payer 1:  {score_a}       Player 2:  {score_b}", align="center", font=("Consola", 14, "bold"))
    
    if coord_x < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        score.clear()
        score.write(f"Payer 1:  {score_a}       Player 2:  {score_b}", align="center", font=("Consola", 14, "bold"))     
    
    if coord_y > 290 or coord_y < -290:
        ball.sety(coord_y)
        ball.dy *= -1
        winsound.PlaySound("plateBreak.wav", winsound.SND_ASYNC)
    
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("plateBreak.wav", winsound.SND_ASYNC)
        
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("plateBreak.wav", winsound.SND_ASYNC)
    
# Funciones para el teclado
wn.listen()
wn.onkeypress(moveUpPaddleA, "w")
wn.onkeypress(moveDownPaddleA, "s")
wn.onkeypress(moveUpPaddleB, "Up")
wn.onkeypress(moveDownPaddleB, "Down")


while True:
    
    wn.update()
    moveBall()
    
