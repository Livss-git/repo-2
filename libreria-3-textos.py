from tkinter import *
from PIL import image, imageTK

ventana = Tk()
ventana.geometry("700x500")

texto = Label(ventana, text="Bienvenido a mi programa").pack(anchor=W)
imagen = Image.open('./C:\primer repo git\icono buscar por imagen google.jpg')
render = imageTK.photoimage(imagen)

ventana.mainloop()