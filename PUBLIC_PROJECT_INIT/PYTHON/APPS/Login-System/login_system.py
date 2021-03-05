from tkinter import *
import pymysql
from tkinter import messagebox

# Los colores se pueden encontrar aqui: https://www.colorhexa.com/color-names
# Funcion Menu principal
def menuPantalla():
    """Muestra la pantalla de Acceso al sistema."""
    
    global pantalla
    pantalla = Tk()
    pantalla.geometry("300x380")
    pantalla.resizable(0, 0)
    pantalla.title("Login System")
    pantalla.iconbitmap("login.ico")
    

    # Para colocar una imagen como etiqueta. Trabaja mejor con formato gif
    image = PhotoImage(file="login.gif")
    image_dim = image.subsample(4, 4) # Para dimensionar la imagen
    image_label = Label(pantalla, image=image_dim) # Poner en etiqueta la imagen
    image_label.pack()

    # Etiqueta de Acceso al sistema
    sys_label = Label(pantalla, text="ACCESO AL SISTEMA", bg="#002e63", fg="white", width=300, height=3, font=("Helvetica", 15, "bold"))
    sys_label.pack()
    space_label = Label(pantalla, text="") # Para tener un espacio separador y no esten pegados
    space_label.pack()

    # Botones -- Inicio de sesion -- Registrarse
    boton_inicio = Button(pantalla, text="Iniciar sesión", width=30, height=3, command=inicioSesion, bg="#007ba7", fg="white", font=("Helvetica", 10, "bold"))
    boton_inicio.pack()
    space_label = Label(pantalla, text="") # Para tener un espacio separador y no esten pegados
    space_label.pack()
    boton_regist = Button(pantalla, text="Registrarse", width=30, height=3, command=registrar, bg="#007ba7", fg="white", font=("Helvetica", 10, "bold"))
    boton_regist.pack()

    pantalla.mainloop()

# Funcion para Inicio de Sesion
def inicioSesion():
    """Muestra la pantalla de inicio de sesión"""
    global pantalla_1
    pantalla_1 = Toplevel(pantalla) # Para hacer que esta pantalla saldrá después de la principal cuando se de click allí
    pantalla_1.geometry("400x250")
    pantalla_1.resizable(0, 0)
    pantalla_1.title("Iniciar Sesión")
    pantalla_1.iconbitmap("iniciosesion.ico")

    # Etiqueta para la presentacion
    intro = "Por favor ingrese su Usuario y Contraseña \n a continuación"
    encabezado_label = Label(pantalla_1, text=intro, bg="#002e63", fg="white", width=300, height=3, font=("Helvetica", 12, "bold"))
    encabezado_label.pack()

    # Variables globales a utilizar
    global usuario_verify
    global contrasena_verify

    # Para editar los widgets y validar datos
    usuario_verify = StringVar()
    contrasena_verify = StringVar()

    global usuario_entry
    global contrasena_entry

    # Etiquetas para usuario y contrseña
    usuario_label = Label(pantalla_1, text="Usuario")
    usuario_label.pack()
    usuario_entry = Entry(pantalla_1, textvariable=usuario_verify)
    usuario_entry.pack()
    Label(pantalla_1, text="").pack() # Para agregar espacio

    contrasena_label = Label(pantalla_1, text="Contraseña")
    contrasena_label.pack()
    contrasena_entry = Entry(pantalla_1, show="*",textvariable=contrasena_verify) # Show es para esconder lo que se escribe.
    contrasena_entry.pack()
    Label(pantalla_1, text="").pack() # Para agregar espacio

    # Boton para iniciar sesion
    boton_inicio_1 = Button(pantalla_1, text="Iniciar Sesión", command=validar_datos, width=12, height=1, bg="#007ba7", fg="white", font=("Helvetica", 10, "bold"))
    boton_inicio_1.pack()

# Funcion de Registrar
def registrar():
    """Muestra ventana de Registrar"""
    global pantalla_2
    pantalla_2 = Toplevel(pantalla)
    pantalla_2.geometry("400x250")
    pantalla_2.resizable(0, 0)
    pantalla_2.title("Registrar")
    pantalla_2.iconbitmap("register.ico")

    # Etiqueta para la presentacion
    intro2 = "Por favor ingrese un Usuario y Contraseña \n para registrarse en el sistema"
    encabezado_label = Label(pantalla_2, text=intro2, bg="#002e63", fg="white", width=300, height=3, font=("Helvetica", 12, "bold"))
    encabezado_label.pack()
    Label(pantalla_2, text="").pack()

    # Etiqueta para el registro de usuario y contrseña
    global usuario_entry_2
    global contrasena_entry_2
    global usuario_label_2
    global contrasena_label_2


    usuario_entry_2 = StringVar()
    contrasena_entry_2 = StringVar()

    usuario_label_2 = Label(pantalla_2, text="Usuario")
    usuario_label_2.pack()
    usuario_entry_2 = Entry(pantalla_2)
    usuario_entry_2.pack()
    Label(pantalla_2, text="").pack()

    contrasena_label_2 = Label(pantalla_2, text="Contraseña")
    contrasena_label_2.pack()
    contrasena_entry_2 = Entry(pantalla_2, show="*") # Show es para esconder lo que se escribe
    contrasena_entry_2.pack()
    Label(pantalla_2, text="").pack()

    # Boton del registro
    boton_regist_2 = Button(pantalla_2, text="Registrarse", width=12, height=1, bg="#007ba7", fg="white", font=("Helvetica", 10, "bold"), command=insertar_datos)
    boton_regist_2.pack()


#####################################################--PARTE2--############################################

# Codigo para conectarse con la base de datos mysql y almacenar los datoss
def insertar_datos():
    """Se conecta e inserta los datos y se almacena en la base de datos mysql"""
    bd = pymysql.connect(
        host= "localhost",
        user= "root",
        passwd= "",
        db="base_datos"
    )
    fcursor = bd.cursor()
    #Se va a insertar todo lo que el usuario digite
    sql = "INSERT INTO login (usuario, contrasena) VALUES ('{0}', '{1}')".format(usuario_entry_2.get(), contrasena_entry_2.get())

    try:
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Registro Exitoso", title="Aviso") #Un mensaje en una ventana aparte
    except:
        bd.rollback()
        messagebox.showinfo(message="No se pudo registrar", title="Aviso")

    bd.close()

# Funcion para validar datos de inicio de sesion
def validar_datos():
    bd = pymysql.connect(
        host= "localhost",
        user= "root",
        passwd= "",
        db="base_datos"
    )

    fcursor = bd.cursor()
    sql_1 = "SELECT contrasena FROM login WHERE usuario='"+usuario_verify.get()+"' and contrasena='"+contrasena_verify.get()+"'"
    fcursor.execute(sql_1)

    if fcursor.fetchall():
        messagebox.showinfo(message="Usuario y contraseña correctos", title="Inicio de sesión correcto")
    else:
        messagebox.showerror(message="Usuario y/o contraseña incorrectos", title="Inicio de sesión incorrecto")

    bd.close()

menuPantalla()