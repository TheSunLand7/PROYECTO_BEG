from tkinter import *
import parser

ventana = Tk()
ventana.geometry("305x300")
ventana.title("Calculadora simple")
ventana.iconbitmap("calculadora.ico")

# Funcionalidades
i = 0
def click_boton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1

def borrar():
    e_texto.delete(0, END)

def get_operacion(operator):
    global i
    operacion_long = len(operator)
    e_texto.insert(i, operator)
    i += operacion_long


""" Para eliminar un dígito a la vez

def undo():
    e_texto_state = e_texto.get()
    if len(e_texto_state):
        e_texto_new_state = e_texto_state[:-1]
        borrar()
        e_texto.insert(0, e_texto_new_state)
    else:
        borrar()
        e_texto.insert(0, "Error")
"""

def get_resultado():
    e_texto_state = e_texto.get()
    try:
        math_expression = parser.expr(e_texto_state).compile()
        result = eval(math_expression)
        borrar()
        e_texto.insert(0, result)
    except Exception as e:
        borrar()
        e_texto.insert(0, "Error")


# Columnspan es para decir que va a haber 4 columnas abajo.
e_texto = Entry(ventana, font=("TerminessTTF Nerd Font", 20, "bold"), justify=RIGHT)
e_texto.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Botones
boton1 = Button(ventana, text="1", bd="5", width=5, height=2, command=lambda: click_boton(1), cursor="hand2")
boton2 = Button(ventana, text="2", bd="5", width=5, height=2, command=lambda: click_boton(2), cursor="hand2")
boton3 = Button(ventana, text="3", bd="5", width=5, height=2, command=lambda: click_boton(3), cursor="hand2")
boton4 = Button(ventana, text="4", bd="5", width=5, height=2, command=lambda: click_boton(4), cursor="hand2")
boton5 = Button(ventana, text="5", bd="5", width=5, height=2, command=lambda: click_boton(5), cursor="hand2")
boton6 = Button(ventana, text="6", bd="5", width=5, height=2, command=lambda: click_boton(6), cursor="hand2")
boton7 = Button(ventana, text="7", bd="5", width=5, height=2, command=lambda: click_boton(7), cursor="hand2")
boton8 = Button(ventana, text="8", bd="5", width=5, height=2, command=lambda: click_boton(8), cursor="hand2")
boton9 = Button(ventana, text="9", bd="5", width=5, height=2, command=lambda: click_boton(9), cursor="hand2")
boton0 = Button(ventana, text="0", bd="5", width=16, height=2, command=lambda: click_boton(0), cursor="hand2")

boton_AC = Button(ventana, text="⌂", bd="5", bg="red", width=5, height=2, command=lambda: borrar(), cursor="hand2")
boton_parent1 = Button(ventana, text="(", bd="5", width=5, height=2, command=lambda: get_operacion("("), cursor="hand2")
boton_parent2 = Button(ventana, text=")", bd="5", width=5, height=2, command=lambda: get_operacion(")"), cursor="hand2")
boton_punto = Button(ventana, text=".", bd="5", width=5, height=2, command=lambda: get_operacion("."), cursor="hand2")

boton_div = Button(ventana, text="÷", bd="5", width=5, height=2, command=lambda: get_operacion("/"), cursor="hand2")
boton_mult = Button(ventana, text="*", bd="5", width=5, height=2, command=lambda: get_operacion("*"), cursor="hand2")
boton_sum = Button(ventana, text="+", bd="5", width=5, height=2, command=lambda: get_operacion("+"), cursor="hand2")
boton_rest = Button(ventana, text="-", bd="5", width=5, height=2, command=lambda: get_operacion("-"), cursor="hand2")
boton_igual = Button(ventana, text="=", width=5, height=2, bd="5", command=lambda: get_resultado(), cursor="hand2")

# Posicionar los botones en pantalla
boton1.grid(row=4, column=0, padx=5, pady=2)
boton2.grid(row=4, column=1, padx=5, pady=2)
boton3.grid(row=4, column=2, padx=5, pady=2)
boton4.grid(row=3, column=0, padx=5, pady=2)
boton5.grid(row=3, column=1, padx=5, pady=2)
boton6.grid(row=3, column=2, padx=5, pady=2)
boton7.grid(row=2, column=0, padx=5, pady=2)
boton8.grid(row=2, column=1, padx=5, pady=2)
boton9.grid(row=2, column=2, padx=5, pady=2)
boton0.grid(row=5, column=0, padx=5, pady=2, columnspan=2)

boton_AC.grid(row=1, column=0, padx=5, pady=2)
boton_parent1.grid(row=1, column=1, padx=5, pady=2)
boton_parent2.grid(row=1, column=2, padx=5, pady=2)
boton_punto.grid(row=5, column=2, padx=5, pady=2)

boton_div.grid(row=1, column=3, padx=5, pady=2)
boton_mult.grid(row=2, column=3, padx=5, pady=2)
boton_sum.grid(row=3, column=3, padx=5, pady=2)
boton_rest.grid(row=4, column=3, padx=5, pady=2)
boton_igual.grid(row=5, column=3, padx=5, pady=2)

ventana.mainloop()
