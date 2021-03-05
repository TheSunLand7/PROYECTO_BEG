from tkinter import *
from tkinter import messagebox
import pymysql

def menuPantallaPrincipal():
    """
    Ventana principal de la aplicación
    """

    global pantalla
    pantalla = Tk()
    pantalla.title("Login System")
    pantalla.geometry("300x380")
    pantalla.resizable(0, 0)
    pantalla.iconbitmap("login.ico")
    # pantalla["background"] = "red" (Opcional)

    imagen = PhotoImage(file="login.gif")
    imagen_dimension = imagen.subsample(4, 4)
    imagen_label = Label(pantalla, image=imagen_dimension, relief="groove")
    imagen_label.pack()
    Label(pantalla, text="").pack()

    presentacion_label = Label(
        pantalla,
        text="ACCESO AL SISTEMA",
        bg="#004225",
        fg="white",
        font=("Helvetica", 15, "bold"),
        width=30,
        height=2
    )
    presentacion_label.pack()
    Label(pantalla, text="").pack()

    boton_iniciar_sesion = Button(
        pantalla,
        text="Iniciar Sesion",
        bg="#004225",
        fg="white",
        font=("Helvetica", 10, "bold"),
        width=20,
        height=2,
        command=iniciarSesion
    )
    boton_iniciar_sesion.pack()
    Label(pantalla, text="").pack()

    boton_registrarse = Button(
        pantalla,
        text="Registrarse",
        bg="#004225",
        fg="white",
        font=("Helvetica", 10, "bold"),
        width=20,
        height=2,
        command=registrar
    )
    boton_registrarse.pack()
    Label(pantalla, text="").pack()

    pantalla.mainloop()

def iniciarSesion():
    """
    Ventana de Iniciar Sesión
    """

    #global pantallaIS
    #global name_usuario_label
    #global name_usuario_entry
    #global password_label
    #global password_entry
    global name_usuario_verify
    global password_verify

    name_usuario_verify = StringVar()
    password_verify = StringVar()

    pantallaIS = Toplevel(pantalla)
    pantallaIS.title("Inicio de Sesión")
    pantallaIS.geometry("400x250")
    pantallaIS.resizable(0, 0)
    pantallaIS.iconbitmap("iniciosesion.ico")

    presentacion_inicio_sesion = Label(
        pantallaIS,
        text="Por favor ingrese su Usuario y Contraseña\n a continuación",
        font=("Helvetica", 14, "bold"),
        bg="#004225",
        fg="white"
    )
    presentacion_inicio_sesion.pack()
    Label(pantallaIS, text="").pack()

    name_usuario_label = Label(pantallaIS, text="Usuario", font=("Helvetica", 10, "bold"))
    name_usuario_label.pack()
    name_usuario_entry = Entry(pantallaIS, textvariable=name_usuario_verify)
    name_usuario_entry.pack()
    Label(pantallaIS, text="").pack()

    password_label = Label(pantallaIS, text="Contrseña", font=("Helvetica", 10, "bold"))
    password_label.pack()
    password_entry = Entry(pantallaIS, textvariable=password_verify, show="*")
    password_entry.pack()
    Label(pantallaIS, text="").pack()

    boton_iniciar_sesion_1 = Button(
        pantallaIS,
        text="Iniciar Sesión",
        font=("Helvetica", 13, "bold"),
        bg="#004225",
        fg="white",
        width=15,
        height=2
    )
    boton_iniciar_sesion_1.pack()

def registrar():
    """
    Ventana del registro del usuario
    """
    
    global pantallaRE
    global name_usuario_reg_entry
    global password_reg_entry

    pantallaRE = Toplevel(pantalla)
    pantallaRE.title("Registro del Usuario")
    pantallaRE.geometry("400x250")
    pantallaRE.resizable(0, 0)
    pantallaRE.iconbitmap("register.ico")

    presentacion_registro = Label(
        pantallaRE, 
        text="Por favor ingrese un Usuario y Contraseña\n a continuación",
        font=("Helvetica", 14, "bold"),
        bg="#004225",
        fg="white"
    )
    presentacion_registro.pack()
    Label(pantallaRE, text="").pack()

    name_usuario_reg = Label(
        pantallaRE,
        text="Usuario",
        font=("Helvetica", 10, "bold")

    )
    name_usuario_reg.pack()
    name_usuario_reg_entry = Entry(pantallaRE)
    name_usuario_reg_entry.pack()
    Label(pantallaRE, text="").pack()
    
    password_reg = Label(pantallaRE, text="Contraseña", font=("Helvetica", 10, "bold"))
    password_reg.pack()
    password_reg_entry = Entry(pantallaRE, show="*")
    password_reg_entry.pack()
    Label(pantallaRE, text="").pack()

    boton_registrarse_1 = Button(
        pantallaRE,
        text="Registrarse",
        font=("Helvetica", 13, "bold"),
        bg="#004225",
        fg="white",
        width=15,
        height=2,
        command=ingresar_datos
    )
    boton_registrarse_1.pack()


def ingresar_datos():
    base_datos = pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="base_datos"
    )

    fcursor = base_datos.cursor()
    insert_data = f"""INSERT INTO login (usuario, contrasena) VALUES ('{name_usuario_reg_entry.get()}',
    '{password_reg_entry.get()}')"""
    
    try:
        fcursor.execute(insert_data)
        base_datos.commit()
        messagebox.showinfo(message="Registro Exitoso", title="Aviso de Registro")
    except:
        base_datos.rollback()
        messagebox.showerror(message="Registro fallido", title="Aviso de Registro")

    base_datos.close()

def validacion_datos():
    base_datos = pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="base_datos"
    )
    fcursor = base_datos.cursor()
    validar_data = "SELECT contrasena FROM login WHERE usuario = '"+name_usuario_verify.get()+"' and contrasena = '"+password_verify.get()+"'"
    fcursor.execute(validar_data)

    if fcursor.fetchall():
        messagebox.showinfo(message="Inicio de Sesión Exitoso", title="Aviso")
    else:
        messagebox.showerror(message="Usuario y/o contraseña incorrecto(s)", title="Aviso")
    
    base_datos.close()

menuPantallaPrincipal()