from tkinter import *

windows_principal = Tk()
windows_principal.title("Calculator")
windows_principal.geometry("305x300")
windows_principal.resizable(0, 0)
windows_principal.iconbitmap("calculadora.ico")


# Entrada de texto
text_entry = Entry(windows_principal, font=("TerminessTTF Nerd Font", 20))
text_entry.pack(padx=5, fill=X)

# BUTTONS
# row 1
Button(windows_principal, text="AC", font=("TerminessTTF Nerd Font", 10, "bold")).place(
	x=5, y=50, anchor="center", width=40, height=30
	)
Button(windows_principal, text="(", font=("TerminessTTF Nerd Font", 10, "bold")).place(
	x=50, y=50, anchor="center", width=40, height=30
	)
Button(windows_principal, text=")", font=("TerminessTTF Nerd Font", 10, "bold")).place(
	x=95, y=50, anchor="center", width=40, height=30
	)
Button(windows_principal, text="/", font=("TerminessTTF Nerd Font", 10, "bold")).place(
	x=140, y=50, anchor="center", width=40, height=30
	)

windows_principal.mainloop()