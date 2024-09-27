from tkinter import *
from tkinter import messagebox

class calculadora:
    
    def __init__(self, alertas):
        self.numero1=StringVar()
        self.numero2=StringVar()
        self.resultado=StringVar()
        

    def cfloat(self, numero):
        try:
            result = float(numero)
        except:
            result = 0
            messagebox.showerror("error", "introduce bien los datos")
        
        return result

    def sumar (self):
        self.resultado.set(self.cfloat (self.numero1.get()) + self.cfloat(self.numero2.get()))
        self.mostrar_resultado()
        
    def restar (self):
        self.resultado.set(self.cfloat (self.numero1.get()) - self.cfloat(self.numero2.get()))
        self.mostrar_resultado()

    def multiplicar (self):
        self.resultado.set(self.cfloat (self.numero1.get()) * self.cfloat(self.numero2.get()))
        self.mostrar_resultado()

    def dividir (self):
        try:
            self.resultado.set(self.cfloat (self.numero1.get()) / self.cfloat(self.numero2.get()))
        except ZeroDivisionError:
            messagebox.showerror("error", "No se puede dividir por cero")
        else:
            self.mostrar_resultado()

    def mostrar_resultado(self):
        messagebox.showinfo("Resultado", f"el resultado de la operacion es: {self.resultado.get()}")
        self.numero1.set("")
        self.numero2.set("")
        
ventana = Tk()
ventana.title("ejercicio completo con tkinter")
ventana.geometry("400x400")
ventana.config(bd=35)

calculadora = calculadora(ventana)
        
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
Entry(marco, textvariable=calculadora.numero1, justify="center").pack()

Label(marco, text="segundo numero"). pack()
Entry(marco, textvariable=calculadora.numero2, justify="center").pack()

Label(marco, text="").pack()

Button(marco, text="sumar", command=calculadora.sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="restar", command=calculadora.restar).pack(side="left", fill=X, expand=YES)
Button(marco, text="multiplicar", command=calculadora.multiplicar).pack(side="left", fill=X, expand=YES)
Button(marco, text="dividir", command=calculadora.dividir).pack(side="left", fill=X, expand=YES)

ventana.mainloop()