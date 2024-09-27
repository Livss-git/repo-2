# calculadora
# dos campos de texto 
# 4 botones para las operaciones 
# mostrar el resultado

from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title("ejercicio completo con tkinter")
ventana.geometry("400x400")
ventana.config(bd=35)

def cfloat(numero):
    try:
        result = float(numero)
    except:
        result = 0
        messagebox.showerror("error", "intrpduce bien los datos")
    
    return result

def sumar ():
    resultado.set(cfloat (numero1.get()) + cfloat(numero2.get()))
    mostrar_resultado()
    
def restar ():
    resultado.set(cfloat (numero1.get()) - cfloat(numero2.get()))
    mostrar_resultado()

def multiplicar ():
    resultado.set(cfloat (numero1.get()) * cfloat(numero2.get()))
    mostrar_resultado()

def dividir ():
    resultado.set(cfloat (numero1.get()) / cfloat(numero2.get()))
    mostrar_resultado()

def mostrar_resultado():
    messagebox.showinfo("Resultado", f"el resultado de la operacion es: {resultado.get()}")

numero1=StringVar()
numero2=StringVar()
resultado=StringVar()

marco = Frame(ventana, width=350, height=200)
marco.config(
    bd=5,
    padx=15,
    pady=15,
    relief=SOLID
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

Label(marco, text="primer numero"). pack()
Entry(marco, textvariable=numero1, justify="center").pack()

Label(marco, text="segundo numero"). pack()
Entry(marco, textvariable=numero2, justify="center").pack()

Label(marco, text="").pack()

Button(marco, text="sumar", command=sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="restar", command=restar).pack(side="left", fill=X, expand=YES)
Button(marco, text="multiplicar", command=multiplicar).pack(side="left", fill=X, expand=YES)
Button(marco, text="dividir", command=dividir).pack(side="left", fill=X, expand=YES)

ventana.mainloop()