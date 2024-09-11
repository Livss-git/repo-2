from tkinter import *

ventana = Tk()
ventana.title("marcos")
ventana.geometry("700x400")

marco = Frame(ventana, width=250, height=250)
marco.config(
    bg="red",
    bd=5,
    relief=SOLID
)
marco.pack(side=RIGHT, anchor=NW)
marco.pack_propagate(False)

Label(marco, text="primer marco").pack()

ventana.mainloop()