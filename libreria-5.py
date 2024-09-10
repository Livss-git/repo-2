from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("750x500")

Label(ventana, Text="hola, soy livan").pack(anchor=W)

Imagen = Image.open('C:\primer repo git\icono buscar por imagen google.jpg')
reader = ImageTk.photoimage(Imagen)

Label(ventana, Image=render).pack(anchor=E)

ventana.mainloop()