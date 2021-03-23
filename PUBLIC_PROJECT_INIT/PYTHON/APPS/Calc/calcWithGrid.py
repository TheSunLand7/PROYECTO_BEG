from tkinter import *

windows_principal = Tk()
windows_principal.title("Calculator")
windows_principal.geometry("340x360")
windows_principal.resizable(0, 0)
windows_principal.iconbitmap("calculadora.ico")


# FUNCTIONS
def numeros(valor):
	global string
	string += str(valor)
	campo.set(string)


def operation():
	global string
	# state = text_entry.get()
	result = eval(text_entry.get())
	campo.set(result)
	"""
	if text_entry.get() in ["+", "-", "*", "/", ".", "(", ")"]:
		pass
	else:
		string = ""
	"""
	string = ""


def delete_all():
	global string
	string = ""
	campo.set(string)
	string = ""


def delete_one():
	global string
	current_state = text_entry.get()
	if len(current_state):
		new_state = current_state[:-1]   # To save from item 1 to item before last item
		delete_all()  # Delete the last item left by new_state
		campo.set(new_state)
	else:
		campo.set("Error, there is no input")


string = ""
campo = StringVar()
# Entrada de texto
text_entry = Entry(windows_principal, font=("TerminessTTF Nerd Font", 16, "bold"), justify=RIGHT, textvariable=campo)
text_entry.grid(row=0, column=0, columnspan=4, pady=7, ipadx=52, ipady=5)

# BUTTONS
# row 1
Button(windows_principal, text="AC", font=("TerminessTTF Nerd Font", 12, "bold"), width=8, height=2, cursor="hand2", command=lambda: delete_all()).grid(
	row=1, column=0, padx=5, pady=2)
Button(windows_principal, text="(", font=("TerminessTTF Nerd Font", 12, "bold"), width=8, height=2, cursor="hand2", command=lambda: numeros("(")).grid(
	row=1, column=1, padx=5, pady=2)
Button(windows_principal, text=")", font=("TerminessTTF Nerd Font", 12, "bold"), width=8, height=2, cursor="hand2", command=lambda: numeros(")")).grid(
	row=1, column=2, padx=5, pady=2)
Button(windows_principal, text="/", font=("TerminessTTF Nerd Font", 12, "bold"), width=8, height=2, cursor="hand2", command=lambda: numeros("/")).grid(
	row=1, column=3, padx=5, pady=2)

# BUTTONS
# row 2
Button(windows_principal, text="7", font=("TerminessTTF Nerd Font", 12, "bold"), width=8, height=2, cursor="hand2", command=lambda: numeros("7")).grid(
	row=2, column=0, padx=5, pady=2)
Button(windows_principal, text="8", font=("TerminessTTF Nerd Font", 12, "bold"), width=8, height=2, cursor="hand2", command=lambda: numeros("8")).grid(
	row=2, column=1, padx=5, pady=2)
Button(windows_principal, text="9", font=("TerminessTTF Nerd Font", 12, "bold"), width=8, height=2, cursor="hand2", command=lambda: numeros("9")).grid(
	row=2, column=2, padx=5, pady=2)
Button(windows_principal, text="x", font=("TerminessTTF Nerd Font", 12, "bold"), width=8, height=2, cursor="hand2", command=lambda: numeros("*")).grid(
	row=2, column=3, padx=5, pady=2)

# BUTTONS
# row 3

Button(windows_principal, text="4", font=("TerminessTTF Nerd Font", 12, "bold"), width=8, height=2, cursor="hand2", command=lambda: numeros("4")).grid(
	row=3, column=0, padx=5, pady=2)
Button(windows_principal, text="5", font=("TerminessTTF Nerd Font", 12, "bold"), width=8, height=2, cursor="hand2", command=lambda: numeros("5")).grid(
	row=3, column=1, padx=5, pady=2)
Button(windows_principal, text="6", font=("TerminessTTF Nerd Font", 12, "bold"), width=8, height=2, cursor="hand2", command=lambda: numeros("6")).grid(
	row=3, column=2, padx=5, pady=2)
Button(windows_principal, text="+", font=("TerminessTTF Nerd Font", 12, "bold"), width=8, height=2, cursor="hand2", command=lambda: numeros("+")).grid(
	row=3, column=3, padx=5, pady=2)

# BUTTONS
# row 4
Button(windows_principal, text="1", font=("TerminessTTF Nerd Font", 12, "bold"), width=8, height=2, cursor="hand2", command=lambda: numeros("1")).grid(
	row=4, column=0, padx=5, pady=2)
Button(windows_principal, text="2", font=("TerminessTTF Nerd Font", 12, "bold"), width=8, height=2, cursor="hand2", command=lambda: numeros("2")).grid(
	row=4, column=1, padx=5, pady=2)
Button(windows_principal, text="3", font=("TerminessTTF Nerd Font", 12, "bold"), width=8, height=2, cursor="hand2", command=lambda: numeros("3")).grid(
	row=4, column=2, padx=5, pady=2)
Button(windows_principal, text="-", font=("TerminessTTF Nerd Font", 12, "bold"), width=8, height=2, cursor="hand2", command=lambda: numeros("-")).grid(
	row=4, column=3, padx=5, pady=2)

# BUTTONS
# row 5
Button(windows_principal, text="0", font=("TerminessTTF Nerd Font", 12, "bold"), width=8, height=2, cursor="hand2", command=lambda: numeros("0")).grid(
	row=5, column=0, padx=5, pady=2)
Button(windows_principal, text=".", font=("TerminessTTF Nerd Font", 12, "bold"), width=8, height=2, cursor="hand2", command=lambda: numeros(".")).grid(
	row=5, column=1, padx=5, pady=2)
Button(windows_principal, text="<--", font=("TerminessTTF Nerd Font", 12, "bold"), width=8, height=2, cursor="hand2", command=lambda: delete_one()).grid(
	row=5, column=2, padx=5, pady=2)
Button(windows_principal, text="=", font=("TerminessTTF Nerd Font", 12, "bold"), width=8, height=2, cursor="hand2", command=lambda: operation()).grid(
	row=5, column=3, padx=5, pady=2)

# row 6
Button(
	windows_principal, text="SALIR", font=("TerminessTTF Nerd Font", 12, "bold"), width=19, height=2, bg="#007fff", fg="#ffffff", cursor="hand2",
	command=windows_principal.destroy).grid(row=6, column=1, padx=5, pady=5, columnspan=2)


windows_principal.mainloop()
