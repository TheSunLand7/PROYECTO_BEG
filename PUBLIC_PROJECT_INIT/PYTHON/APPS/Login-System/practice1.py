# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 17:14:44 2021

@author: SIR Anker
"""
from tkinter import *
from tkinter import messagebox
import pymysql

ventana_principal = Tk()
ventana_principal.title("LOGIN SYSTEM BASIC")
ventana_principal.geometry("305x380")
ventana_principal.resizable(0, 0)
# En tkinter, los iconos de las ventanas van en formato .ico
# Sin embargo, para imagenes dentro de la ventana van en formato
# .gif
ventana_principal.iconbitmap("login.ico")

imagen = PhotoImage(file="login.gif")
imagen_dim = imagen.subsample(5, 5)
Label(ventana_principal, image=imagen_dim, relief="groove").pack()

def main():
    Label(ventana_principal, text="ACCESO AL SISTEMA", bg="#004225", fg="#ffffff",
        font=("TerminessTTF Nerd Font", 20, "bold"), height=2
        ).pack(fill=X, pady=5)
    Label(ventana_principal, text="").pack()

    Button(ventana_principal, text="Iniciar Sesión", fg="#ffffff", bg="#004225",
        font=("TerminessTTF Nerd Font", 12, "bold"), width=20, height=2, command=log_in
    ).place(x=151, y=220, anchor="center")
    Button(ventana_principal, text="Registrarse", fg="#ffffff", bg="#004225",
        font=("TerminessTTF Nerd Font", 12, "bold"), width=20, height=2, command=sign_up
    ).place(x=151, y=300, anchor="center")

    ventana_principal.mainloop()

def log_in():
    ventana_login = Toplevel(ventana_principal)
    ventana_login.title("INICIAR SESIÓN")
    ventana_login.geometry("460x280")
    ventana_login.resizable(0, 0)
    ventana_login.iconbitmap("iniciosesion.ico")

    # #007fff: color medio celeste (o eso creo :v)
    Label(ventana_login, text="Por favor ingrese su usuario y contrseña\n a continuación", bg="#007fff", fg="#ffffff",
        font=("TerminessTTF Nerd Font", 15, "bold"), height=3
        ).pack(fill=X)

    Label(ventana_login, text="Usuario/e-mail",
        font=("TerminessTTF Nerd Font", 15, "bold")
        ).place(x=40, y=100)
    user_entry = Entry(ventana_login, font=("TerminessTTF Nerd Font", 15, "bold"))
    user_entry.place(x=210, y=100, width=180, height=25)

    Label(ventana_login, text="Contraseña",
        font=("TerminessTTF Nerd Font", 15, "bold")
        ).place(x=40, y=150)
    password_entry = Entry(ventana_login, font=("TerminessTTF Nerd Font", 15, "bold"),
    show="●")
    password_entry.place(x=210, y=150, width=180, height=25)

    Button(ventana_login, text="Iniciar Sesión",
    fg="#ffffff", bg="#007fff", width=20, height=2,
    font=("TerminessTTF Nerd Font", 12, "bold")
    ).place(x=270, y=200, anchor="nw")

    Button(ventana_login, text="Cancelar",
    fg="#ffffff", bg="#e32636", width=20, height=2,
    font=("TerminessTTF Nerd Font", 12, "bold"),
    command=ventana_login.destroy
    ).place(x=50, y=200, anchor="nw")

def sign_up():
    global user_sign_entry
    global email_sign_entry
    global password_sign_entry
    global phone_sign_entry
    
    ventana_signup = Toplevel(ventana_principal)
    ventana_signup.title("REGISTRO DE USUARIO")
    ventana_signup.geometry("420x480")
    ventana_signup.resizable(0, 0)
    ventana_signup.iconbitmap("register.ico")

    Label(ventana_signup, text="Por favor REGÍSTRESE",
    bg="#bd33a4", fg="#ffffff", font=("TerminessTTF Nerd Font", 20, "bold"),
    height=2
    ).pack(fill=X)

    #Labels and Entries for user, e-mail, password and phone number
    Label(ventana_signup, text="Usuario",
    font=("TerminessTTF Nerd Font", 15, "bold")
    ).place(x=40, y=100)
    user_sign_entry = Entry(ventana_signup, font=("TerminessTTF Nerd Font", 15, "bold"))
    user_sign_entry.place(x=160, y=100)

    Label(ventana_signup, text="E-mail",
    font=("TerminessTTF Nerd Font", 15, "bold")
    ).place(x=40, y=150)
    email_sign_entry = Entry(ventana_signup, font=("TerminessTTF Nerd Font", 15, "bold"))
    email_sign_entry.place(x=160, y=150)

    Label(ventana_signup, text="Contraseña",
    font=("TerminessTTF Nerd Font", 15, "bold")
    ).place(x=40, y=200)
    password_sign_entry = Entry(ventana_signup, font=("TerminessTTF Nerd Font", 15, "bold"),
    show="●")
    password_sign_entry.place(x=160, y=200)

    Label(ventana_signup, text="Repita su\n contraseña",
    font=("TerminessTTF Nerd Font", 15, "bold")
    ).place(x=31, y=240)
    Entry(ventana_signup, font=("TerminessTTF Nerd Font", 15, "bold"),
    show="●"
    ).place(x=160, y=250)

    Label(ventana_signup, text="Número de\n teléfono",
    font=("TerminessTTF Nerd Font", 15, "bold")
    ).place(x=40, y=300)
    phone_sign_entry = Entry(ventana_signup, font=("TerminessTTF Nerd Font", 15, "bold"))
    phone_sign_entry.place(x=160, y=310)

    # Quiero intentar que cuando ingrese un input, este debe ser integer
    # try:
    #     phone_sign_entry = Entry(ventana_signup, font=("TerminessTTF Nerd Font", 15, "bold"))
    #     phone_sign_entry.place(x=160, y=310)
    # except Exception as e:
    #     print("Invalid input")


    Button(ventana_signup, text="Registrarse",
    fg="#ffffff", bg="#bd33a4", width=20, height=2,
    font=("TerminessTTF Nerd Font", 12, "bold")
    ).place(x=228, y=400, anchor="nw")

    Button(ventana_signup, text="Cancelar",
    fg="#ffffff", bg="#e32636", width=20, height=2,
    font=("TerminessTTF Nerd Font", 12, "bold"),
    command=ventana_signup.destroy
    ).place(x=30, y=400, anchor="nw")

def insert_data():
    data_base = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="name of data base"
    )

    db_cursor = data_base.cursor()
    insert = "INSERT INTO signup (Usuario, Mail, Password, Phonenumber) VALUES"
    sql = f"""insert ('{user_sign_entry.get()}', '{email_sign_entry.get()}', '{password_sign_entry.get()}',
     '{phone_sign_entry.get()}'
    )"""

    try:
        db_cursor.execute(sql)
        data_base.commit()
        messagebox.showinfo(message="Registro Exitoso", title="AVISO")
    except Exception as e:
        data_base.rollback()
        messagebox.showerror(message="No se pudo registrar!", title="AVISO")

    data_base.close()

def verify_data():
    data_base = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="name of the data base"
    )

    db_cursor = data_base.cursor()
    verify = "SELECT Password FROM signup WHERE Usuario='"++"' and Password='"++"'"
    db_cursor.execute(verify)

    data_base.close()

if __name__ == '__main__':
    main()
