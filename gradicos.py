from tkinter import *

# crea ventana
ventana = Tk()
ventana.geometry("420x300")
ventana.resizable(0,1)
ventana.title("mi primer ventana en python")
ventana.iconbitmap("diamond.ico")
texto=Label(ventana,text="hola mundo")
texto.config(fg="red",bg="#000000"
)
texto.pack()

# este metodo va al final 
ventana.mainloop()