from tkinter import *

ventana = Tk()
ventana.geometry("700x400")
ventana.title("formularios de tkinter")


encabezado = Label(ventana, text="formularios con tkinter")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("open Sans", 18),
    padx=10,
    pady=10
)
encabezado.grid(row=0, column=0, columnspan=12, sticky=E)

# Label para el campo
label = Label(ventana, text="nombre")
label.grid(row=1, column=0, sticky=W, padx=5, pady=5)


# campo de texto
campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="right", state="normal")



label = Label(ventana, text="apellidos")
label.grid(row=2, column=0, sticky=W, padx=5, pady=5)


# campo de texto
campo_texto = Entry(ventana)
campo_texto.grid(row=2, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="right", state="normal")

label = Label(ventana, text="descripccion")
label.grid(row=3, column=0, padx=5, pady=5)

campo_grande = Text(ventana)
campo_grande.grid(row=3, column=1)
campo_grande.config(width=30, height=5)

# botones 

Button,
ventana.mainloop()