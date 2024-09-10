from tkinter import *

ventana = Tk()
ventana.geometry("700x500")

texto = Label(ventana, text="bienvenido a mi programa")
texto.config(
    fg = "black",
    bg = "blue",
    padx = 20,
    pady = 20,
    font = ("Arial", 30)
)
texto.pack()

def prueba (nombre, apellidos, pais):
    return f"hola {nombre} {apellidos} veo que eres de {pais}"

texto = Label(ventana, text=prueba(nombre="victor", apellidos="robles", pais="españa"))
texto.config(
    height = 400,
    bg = "orange",
    font = ("arial", 18),
    padx =10,
    pady = 10,
    cursor = "circle"
)
texto.pack(anchor=SE)


ventana.mainloop()