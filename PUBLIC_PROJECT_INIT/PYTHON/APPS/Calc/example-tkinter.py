import tkinter

# Para abrir la ventana en la computadora
ventana = tkinter.Tk()
# Para redimensionar la ventana. Va antes del mainloop
ventana.geometry("600x300")

# La etiqueta sirve para colocarlo en la ventana
"""
etiqueta = tkinter.Label(ventana, text="Calculadora con IA", bg="green", fg="white")
etiqueta.pack(side=tkinter.BOTTOM, fill=tkinter.X)  # Sirve para colocar en la ventana lo que hacemos.
# etiqueta.pack(side=tkinter.BOTTOM, fill=tkinter.Y, expand=True)
# etiqueta.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=True)  # LLenado completo

# Para colocar botones en la ventana. El command se utiliza para agregar funcionalidad al boton
# Para ello se crea una función. También se puede hacer con lambda
# def saludo():
#     print("Bienvenida chatita")
# boton1 = tkinter.Button(ventana, text="Borrar", padx=10, pady=5, command=saludo)
# boton1.pack()

# Si se desea usar parámetros, debemos usar la funcion lambda

def saludo(nombre):
    print("Bienvenido", nombre)
boton1 = tkinter.Button(ventana, text="Borrar", padx=10, pady=5, command=lambda: saludo("Carlos"))
boton1.pack()


# Para agragar cajas de text. Esto te premite escribir desde tu keyboard
cajaTexto = tkinter.Entry(ventana, font="Consolas 20")
cajaTexto.pack()
# Si queremos que lo escrito en la caja de texto aparezca en la consola, creamos una función
def texto():
    text1 = cajaTexto.get() # get sirve para obtener lo que se escribió en la caja de texto
    print(text1)

boton2 = tkinter.Button(ventana, text="Click", command = texto)
boton2.pack()

# Para colocar lo que se escribe en la caja de texto como etiqueta.
etiqueta = tkinter.Label(ventana)
etiqueta.pack()
def texto():
    text1 = cajaTexto.get()
    etiqueta["text"] = text1
boton2 = tkinter.Button(ventana, text="Click", command = texto)
boton2.pack()
"""

# Usando el metodo GRID para crear una tabla. BD es para darles mayor volumen a los bordes
# destroy sirve para desaparecer la ventana una vez se de click en un boton
boton1 = tkinter.Button(ventana, text="Boton1", bd="5", command=ventana.destroy)
boton2 = tkinter.Button(ventana, text="Boton2", bd="5")
boton3 = tkinter.Button(ventana, text="Boton3", bd="5")

boton1.grid(row=0, column=0, padx=5, pady=2)
boton2.grid(row=0, column=1, padx=5, pady=2)
boton3.grid(row=0, column=2, padx=5, pady=2)
# Lleva el registro de lo que esta sucediendo en la ventana
ventana.mainloop()
