import turtle, time, random
from tkinter import messagebox

posponer = 0.1

#Marcador
actual_score = 0
high_score = 0

# Screen settings
wn = turtle.Screen()
wn.title("Juego de Snake BEGINNER")
wn.setup(width=600, height=600)
wn.bgcolor("black")
wn.tracer(0)


# Snake's food
comida = turtle.Turtle()
comida.shape("circle")
comida.speed(0)
comida.color("red")
comida.penup() # Para que no deje huella la tortuga
comida.goto(0,100) # Para indicar la posición inicial de la comida

# Turtle on the screen
tortuga = turtle.Turtle()
tortuga.shape("square")
tortuga.speed(0)
tortuga.color("blue")
tortuga.penup() # Para que no deje huella la tortuga
tortuga.goto(0,0) # Para indicar la posición inicial de la tortuga
tortuga.direction = "stop"

# Funciones de movement
def go_up():
    tortuga.direction = "up"
def go_down():
    tortuga.direction = "down"
def go_left():
    tortuga.direction = "left"
def go_right():
    tortuga.direction = "right"


def mov():
    if tortuga.direction == "up":
        y1 = tortuga.ycor()
        y1 += 20
        tortuga.sety(y1)

    if tortuga.direction == "down":
        y2 = tortuga.ycor()
        y2 -= 20
        tortuga.sety(y2)

    if tortuga.direction == "right":
        x1 = tortuga.xcor()
        x1 += 20
        tortuga.setx(x1)

    if tortuga.direction == "left":
        x2 = tortuga.xcor()
        x2 -= 20
        tortuga.setx(x2)

def main():
    global actual_score
    global high_score
    # Para conectar con el teclado
    wn.listen()
    wn.onkeypress(go_up, "Up")
    wn.onkeypress(go_down, "Down")
    wn.onkeypress(go_left, "Left")
    wn.onkeypress(go_right, "Right")

    #Cuerpo de la serpiente
    colas_add = list()

    # Texto en pantalla
    score_text = turtle.Turtle()
    score_text.speed(0)
    score_text.color("#ffffff")
    score_text.penup()
    score_text.hideturtle()
    score_text.goto(0, 260)
    score_text.write("Actual Score: 0        High Score: 0",
               align="center", font=("TerminessTTF Nerd Font", 18, "bold")
               )


    while True:
        wn.update()

        #Choque con los bordes de la ventana
        if tortuga.xcor()>280 or tortuga.xcor()<-280 or tortuga.ycor()>280 or tortuga.ycor()<-280:
            messagebox.showwarning(message="Oh no! Has chocado con el borde!", title="Aviso del juego")
            time.sleep(1)
            tortuga.goto(0, 0)
            tortuga.direction = "stop"

            #To hide la cola
            for cola in colas_add:
                cola.goto(1000,1000)
            # To clear list of colas
            colas_add.clear()

            #Resetear el marcador
            actual_score = 0
            score_text.clear()
            score_text.write(f"Actual Score: {actual_score}        High Score: {high_score}",
               align="center", font=("TerminessTTF Nerd Font", 18, "bold")
               )

        # Choques con la comida
        if tortuga.distance(comida)<20:
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            comida.goto(x, y)

            cola_snake = turtle.Turtle()
            cola_snake.shape("square")
            cola_snake.speed(0)
            cola_snake.color("#007fff")
            cola_snake.penup() # Para que no deje huella la tortuga
            colas_add.append(cola_snake)

            # Aumentar el marcador en la pantalla
            actual_score += 10
            if actual_score > high_score:
                high_score = actual_score
            score_text.clear()
            score_text.write(f"Actual Score: {actual_score}        High Score: {high_score}",
                        align="center", font=("TerminessTTF Nerd Font", 18, "bold")
                       )

        # To move snake's body||| no entiendo esta parte uu :'('
        totalColas = len(colas_add)
        for index in range(totalColas-1, 0, -1):
            x = colas_add[index-1].xcor()
            y = colas_add[index-1].ycor()
            colas_add[index].goto(x, y)

        if totalColas > 0:
            x = tortuga.xcor()
            y = tortuga.ycor()
            colas_add[0].goto(x, y)

        mov()

        #Choques con las colas
        for cola in colas_add:
            if cola.distance(tortuga) < 20:
                messagebox.showwarning(message="Oh no! Has chocado con tu cola!", title="Aviso del juego")
                time.sleep(1)
                tortuga.goto(0, 0)
                tortuga.direction = "stop"

                # Esconder las colas
                for cola in colas_add:
                    cola.goto(1000, 1000)
                colas_add.clear()

                #Resetear el marcador
                actual_score = 0
                score_text.clear()
                score_text.write(f"Actual Score: {actual_score}        High Score: {high_score}",
                                align="center", font=("TerminessTTF Nerd Font", 18, "bold")
                                )

        time.sleep(posponer)

main()
wn.mainloop()
