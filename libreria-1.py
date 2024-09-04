from tkinter import *

# crea ventana
ventana = Tk()

# tamaño ventana 
ventana.geometry("420x300")

# dimenciones fijas de la ventana
ventana.resizable(0,1)

# titulo de la ventana 
ventana.title("mi primer ventana en python")

# icono de la ventana 
ventana.iconbitmap("diamond.ico")

# texto de la ventana
texto=Label(ventana,text="hola mundo")

# color del texto de la ventana
texto.config(fg="red",bg="#000000"
)
texto.pack()

# este metodo va al final 
ventana.mainloop()