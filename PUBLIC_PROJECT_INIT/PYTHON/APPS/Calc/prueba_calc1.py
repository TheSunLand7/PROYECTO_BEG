from tkinter import *


# Ventana
ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("305x280")
ventana.resizable(0, 0)
ventana.configure(background="gray")
ventana.iconbitmap("calculadora.ico")

# FUNCIONALIDADES
# Funcion numeros
def numeros(valor):
    global cadena
    cadena = cadena + str(valor)
    campo.set(cadena)

# Funcion borrar
def eliminar():
    global cadena
    cadena = ""
    campo.set("")

# Funcion operaciones
def operacion():
    global cadena
    resultado = str(eval(cadena))
    campo.set(resultado)
    cadena = ""

cadena = ""
# El StringVar() sirve para editar un texto de widget
campo = StringVar()

# Entrada de texto
e_text = Entry(ventana, font=("TerminessTTF Nerd Font", 20, "bold"), bd="5", bg="lightgray", fg="black", justify= RIGHT, textvariable=campo)
e_text.grid(row=0, column=0, columnspan=4, padx=2, pady=2)

# BUTTINS FOR ROWS
# row 1
borrar = Button(ventana, text="AC", bd=5, bg="red", fg="black", font="bold", width=3, height=1, command=lambda: eliminar(), cursor="hand2")
paren1 = Button(ventana, text="(", bd="5", bg="gray", fg="black", font="bold", width=3, height=1, command=lambda: numeros("("), cursor="hand2")
paren2 = Button(ventana, text=")", bd="5", bg="gray", fg="black", font="bold", width=3, height=1, command=lambda: numeros(")"), cursor="hand2")
divi = Button(ventana, text="/", bd="5", bg="gray", fg="black", font="bold", width=3, height=1, command=lambda: numeros("/"), cursor="hand2")
# row 2
tecla_7 = Button(ventana, text="7", bd="5", bg="gray", fg="black", font="bold", width=3, height=1, command=lambda: numeros(7), cursor="hand2")
tecla_8 = Button(ventana, text="8", bd="5", bg="gray", fg="black", font="bold", width=3, height=1, command=lambda: numeros(8), cursor="hand2")
tecla_9 = Button(ventana, text="9", bd="5", bg="gray", fg="black", font="bold", width=3, height=1, command=lambda: numeros(9), cursor="hand2")
tecla_mult = Button(ventana, text="*", bd="5", bg="gray", fg="black", font="bold", width=3, height=1, command=lambda: numeros("*"), cursor="hand2")
# row 3
tecla_4 = Button(ventana, text="4", bd="5", bg="gray", fg="black", font="bold", width=3, height=1, command=lambda: numeros(4), cursor="hand2")
tecla_5 = Button(ventana, text="5", bd="5", bg="gray", fg="black", font="bold", width=3, height=1, command=lambda: numeros(5), cursor="hand2")
tecla_6 = Button(ventana, text="6", bd="5", bg="gray", fg="black", font="bold", width=3, height=1, command=lambda: numeros(6), cursor="hand2")
tecla_mas = Button(ventana, text="+", bd="5", bg="gray", fg="black", font="bold", width=3, height=1, command=lambda: numeros("+"), cursor="hand2")
# row 4
tecla_1 = Button(ventana, text="1", bd="5", bg="gray", fg="black", font="bold", width=3, height=1, command=lambda: numeros(1), cursor="hand2")
tecla_2 = Button(ventana, text="2", bd="5", bg="gray", fg="black", font="bold", width=3, height=1, command=lambda: numeros(2), cursor="hand2")
tecla_3 = Button(ventana, text="3", bd="5", bg="gray", fg="black", font="bold", width=3, height=1, command=lambda: numeros(3), cursor="hand2")
tecla_menos = Button(ventana, text="-", bd="5", bg="gray", fg="black", font="bold", width=3, height=1, command=lambda: numeros("-"), cursor="hand2")
# row 5
tecla_0 = Button(ventana, text="0", bd="5", bg="gray", fg="black", font="bold", width=3, height=1, command=lambda: numeros(0), cursor="hand2")
tecla_pot = Button(ventana, text="^", bd="5", bg="gray", fg="black", font="bold", width=3, height=1, command=lambda: numeros("**"), cursor="hand2")
tecla_punto = Button(ventana, text=".", bd="5", bg="gray", fg="black", font="bold", width=3, height=1, command=lambda: numeros("."), cursor="hand2")
tecla_igual = Button(ventana, text="=", bd="5", bg="gray", fg="black", font="bold", width=3, height=1, command=lambda: operacion(), cursor="hand2")

# GRIDS FOR ROWS
# row 1
borrar.grid(row=1, column=0, sticky=W+E)
paren1.grid(row=1, column=1, sticky=W+E)
paren2.grid(row=1, column=2, sticky=W+E)
divi.grid(row=1, column=3, sticky=W+E)

# row 2
tecla_7.grid(row=2, column=0, sticky=W+E)
tecla_8.grid(row=2, column=1, sticky=W+E)
tecla_9.grid(row=2, column=2, sticky=W+E)
tecla_mult.grid(row=2, column=3, sticky=W+E)

# row 3
tecla_4.grid(row=3, column=0, sticky=W+E)
tecla_5.grid(row=3, column=1, sticky=W+E)
tecla_6.grid(row=3, column=2, sticky=W+E)
tecla_mas.grid(row=3, column=3, sticky=W+E)

# row 4
tecla_1.grid(row=4, column=0, sticky=W+E)
tecla_2.grid(row=4, column=1, sticky=W+E)
tecla_3.grid(row=4, column=2, sticky=W+E)
tecla_menos.grid(row=4, column=3, sticky=W+E)

# row 5
tecla_0.grid(row=5, column=0, sticky=W+E)
tecla_pot.grid(row=5, column=1, sticky=W+E)
tecla_punto.grid(row=5, column=2, sticky=W+E)
tecla_igual.grid(row=5, column=3, sticky=W+E)

ventana.mainloop()
