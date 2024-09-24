from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.config(bd=70)

def sacarAlerta():
    MessageBox.showinfo("alerta", "hola soy victor robles")

Button(ventana, text="mostrar alerta", command=sacarAlerta()).pack()

ventana.mainloop()