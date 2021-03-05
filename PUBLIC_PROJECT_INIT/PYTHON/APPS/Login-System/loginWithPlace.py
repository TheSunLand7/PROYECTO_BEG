from tkinter import *
from tkinter import messagebox
import pymysql

# Principal screen
windows_principal = Tk()
windows_principal.title("LOGIN SYSTEM")
windows_principal.geometry("305x380")
windows_principal.resizable(0, 0)
windows_principal.iconbitmap("login.ico")

# Labels
imagen = PhotoImage(file="login.gif")
imagen_dim = imagen.subsample(5, 5)
Label(windows_principal, image=imagen_dim, relief="groove").pack()


def menu_principal():
	"""First screen"""
	# Labels
	Label(windows_principal, text="ACCESO AL SISTEMA", bg="#004225", fg="#ffffff",
		font=("TerminessTTF Nerd Font", 20, "bold"), height=2
		).pack(pady=5, fill=X)
	Label(windows_principal, text="").pack()

	# Buttons
	Button(windows_principal, text="Iniciar Sesión", bg="#004225", fg="#ffffff",
		font=("TerminessTTF Nerd Font", 12, "bold"), width=20, height=2, command=log_in
		).place(x=151, y=220, anchor="center")
	Button(windows_principal, text="Registrarse", bg="#004225", fg="#ffffff",
		font=("TerminessTTF Nerd Font", 12, "bold"), width=20, height=2, command=sign_up
		).place(x=67, y=280)

	windows_principal.mainloop()

def log_in():
	"""Window of Log in"""

	global user_verify
	global password_verify

	user_verify = StringVar()
	password_verify = StringVar()

	windows_login = Toplevel(windows_principal)
	windows_login.title("Iniciar Sesión")
	windows_login.geometry("460x280")
	windows_login.resizable(0, 0)
	windows_login.iconbitmap("iniciosesion.ico")

	#Label text
	Label(windows_login, text="Por favor ingrese su usuario y contraseña\n a continuación",
		fg="#ffffff", bg="#007fff", font=("TerminessTTF Nerd Font", 15, "bold"), height=3
		).pack(fill=X)

	# Label and Entry for user
	Label(windows_login, text="Usuario/e-mail",
		font=("TerminessTTF Nerd Font", 15, "bold")
		).place(x=40, y=100)
	user_entry = Entry(windows_login, font=("TerminessTTF Nerd Font", 15, "bold"),
		textvariable=user_verify)
	user_entry.place(x=210, y=100, width=180, height=25)
	# Label and Entry for password
	Label(windows_login, text="Contraseña",
		font=("TerminessTTF Nerd Font", 15, "bold")
		).place(x=40, y=150)
	password_entry = Entry(windows_login, font=("TerminessTTF Nerd Font", 15, "bold"), 
		show="*", textvariable=password_verify)
	password_entry.place(x=210, y=150, width=180, height=25)

	#Button Log In
	Button(windows_login, text="Iniciar Sesión",
		fg="#ffffff", bg="#007fff", width=20, height=2,
		font=("TerminessTTF Nerd Font", 12, "bold"),
		command=verify_data
		).place(x=270, y=200, anchor="nw")
	#Button Cancel
	Button(windows_login, text="Cancelar",
		fg="#ffffff", bg="#e32636", width=20, height=2,
		font=("TerminessTTF Nerd Font", 12, "bold"),
		command=windows_login.destroy
		).place(x=50, y=200, anchor="nw")

def sign_up():
	"""Window of Sign up"""

	global user_sign_entry
	global password_sign_entry
	global email_sign_entry
	global phone_sign_entry

	windows_signup = Toplevel(windows_principal)
	windows_signup.title("Registro de usuario")
	windows_signup.geometry("420x480")
	windows_signup.resizable(0, 0)
	windows_signup.iconbitmap("register.ico")

	Label(windows_signup, text="Por favor REGÍSTRESE",
		bg="#bd33a4", fg="#ffffff", font=("TerminessTTF Nerd Font", 20, "bold"),
		height=2
		).pack(fill=X)

	# Label and Entries for user, e-mail, password and phone number
	Label(windows_signup, text="Usuario", 
		font=("TerminessTTF Nerd Font", 15, "bold")
		).place(x=40, y=100)
	user_sign_entry = Entry(windows_signup, font=("TerminessTTF Nerd Font", 15, "bold"))
	user_sign_entry.place(x=160, y=100)

	Label(windows_signup, text="e-mail", 
		font=("TerminessTTF Nerd Font", 15, "bold")
		).place(x=40, y=150)
	email_sign_entry = Entry(windows_signup, font=("TerminessTTF Nerd Font", 15, "bold"))
	email_sign_entry.place(x=160, y=150)

	Label(windows_signup, text="Contraseña", 
		font=("TerminessTTF Nerd Font", 15, "bold")
		).place(x=40, y=200)
	password_sign_entry = Entry(windows_signup, font=("TerminessTTF Nerd Font", 15, "bold"),
		show="*")
	password_sign_entry.place(x=160, y=200)

	Label(windows_signup, text="Repita su\n contraseña", 
		font=("TerminessTTF Nerd Font", 15, "bold")
		).place(x=31, y=240)
	Entry(windows_signup, font=("TerminessTTF Nerd Font", 15, "bold"),
		show="*"
		).place(x=160, y=250)

	Label(windows_signup, text="Número de\n teléfono", 
		font=("TerminessTTF Nerd Font", 15, "bold")
		).place(x=40, y=300)
	phone_sign_entry = Entry(windows_signup, font=("TerminessTTF Nerd Font", 15, "bold"))
	phone_sign_entry.place(x=160, y=310)

	#Button Sign Up
	Button(windows_signup, text="Registrarse",
		fg="#ffffff", bg="#bd33a4", width=20, height=2,
		font=("TerminessTTF Nerd Font", 12, "bold"), command=insert_data
		).place(x=228, y=400, anchor="nw")
	#Button Cancel
	Button(windows_signup, text="Cancelar",
		fg="#ffffff", bg="#e32636", width=20, height=2,
		font=("TerminessTTF Nerd Font", 12, "bold"),
		command=windows_signup.destroy
		).place(x=30, y=400, anchor="nw")

def insert_data():
	data_base = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="Proyecto1"
    )

	db_cursor = data_base.cursor() # Para ir a l db y buscar info
	sql = f"""INSERT INTO signup (Usuario, Mail, Password, Phonenumber) VALUES (
			'{user_sign_entry.get()}', '{email_sign_entry.get()}', '{password_sign_entry.get()}',
			'{phone_sign_entry.get()}'
			)"""

	try:
		db_cursor.execute(sql)
		data_base.commit()
		messagebox.showinfo(message="Registro Exitoso", title="Aviso")
	except Exception as e:
		data_base.rollback()
		messagebox.showerror(message="No se pudo registrar", title="Aviso")

	data_base.close()

def verify_data():

	data_base = pymysql.connect(
		host="localhost",
		user="root",
		password="",
		db="Proyecto1"
		)

	db_cursor = data_base.cursor()
	sql = "SELECT Password FROM signup WHERE Usuario='"+user_verify.get()+"' and Password='"+password_verify.get()+"'"
	db_cursor.execute(sql)

	if db_cursor.fetchall():
		messagebox.showinfo(message="Inicio de Sesión Exitoso", title="Aviso")
	else:
		messagebox.showerror(message="No se pudo iniciar sesión", title="Aviso")

	data_base.close()

menu_principal()

# Cosas que me faltan
"""
1. Que el usuario ingrese a la plataforma con su usurio y/o email
2. Hacer que ingresar contraseña y repetir contrseña coincidan y si no,
   que de un error y que vuelva a intentarlo
3. Aprender un poco más sobre data base 
"""