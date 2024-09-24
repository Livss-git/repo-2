from tkinter import *

ventana = Tk()
ventana.geometry("700x500")

ventana.config(
    bd=50
)

def getDato():
    resultado.set(dato.get())
    
    if len(resultado.get()) >= 1:
        texto_recogido.config(
    bg="green", 
    fg="white"
)

dato=StringVar()
resultado=StringVar

Label(ventana, text="mete un texto").pack(anchor=NW)
Entry(ventana, textvariable=dato).pack(anchor=NW)

Label(ventana, text="dato recogido: ").pack(anchor=NW)
texto_recogido = Label(ventana, textvariable=resultado)

Button(ventana, text="mostrar datos", command=getDato).pack(anchor=NW)

ventana.mainloop()