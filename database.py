import tkinter as tk 
from tkinter import messagebox
import psycopg2

def conectar_db ():
    try:
        conn = psycopg2.connect(
            dbname='conectar',
            user='postgres',
            password='livan123',
            host = 'localhost',
            port = '5432'
        )
        print ("conectado exitosamente")
        return conn
    except psycopg2.Error as e:
        messagebox.showerror("error de coneccion", f"no se pudo conectar a la base de datos: {e}");
        exit()
    
def agregar_venta():
    id = entry_id.get()
    nombre = entry_nombre.get()
    venta = entry_venta.get()
    sucursal = entry_sucursal.get()
    
    if nombre and venta and sucursal:
        try:
            conn =conectar_db()
            c = conn.cursor()
            c.execute("insetr into venta (id, nombre, venta, sucursal,) VALUES (%s, %s, %s, %s)",
                      (id, nombre, venta, sucursal))
            conn.comit()
            c.close()
            conn.close()
            messagebox.showinfo("exito", "venta registrada correctamente")
            limpiar_formulario()
        except psycopg2.Error  as e:
            messagebox.showerror("Error", f"Error al agregar la venta: {e}")
    else: messagebox.showwarning("adventencia", "por favor, completa todos los campos")
    
# limpiar el formulario    
def limpiar_formulario():
    entry_id.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_venta.delete(0, tk.END)
    entry_sucursal.delete(0, tk.END)
    
    
# venta para consultar por id
def abrir_ventana_consulta ():
    consulta_ventana = tk.Toplevel(root)
    consulta_ventana.title =("consulta de ventana por id")
    consulta_ventana.geometry = ("300x200")
    
    tk.Label(consulta_ventana, text="ingrese id").pack(pady=10)
    entry_id_consulta = tk.Entry(consulta_ventana)
    entry_id_consulta.pack()
    
    # def consultar():
    #     id_consulta = entry_id_consulta.get()
    #     if id_consulta:
    #         try:
    #             conn = conectar_db()
    #             c = conn.cursor()
    #             c.execute 
    
# configuracion de la ventana principal
root = tk.tk()
root.title("regisro de ventas")
root.geometry("300x200")

# crear tabla 

# etiquetas y campos de entrada 
tk.Label(root, text="id").pack(pady=5)
entry_id = tk.Entry(root)
entry_id.pack()

tk.Label(root, text="nombre").pack(pady=5)
entry_nombre = tk.Entry(root)
entry_nombre.pack()

tk.Label(root, text="venta").pack(pady=5)
entry_venta = tk.Entry(root)
entry_venta.pack()

tk.Label(root, text="sucursal").pack(pady=5)
entry_sucursal = tk.Entry(root)
entry_sucursal.pack()

# boton para agregar la ventana 
btn_agregar = tk.Button(root, text="agreagr ventana", command = agregar_venta)
btn_agregar.pack(pady=10) 

# boton para abrir la ventana de consulta  
btn_agregar = tk.Button(root, text="consulta ventana por id", command = abrir_venta_consulta)
btn_consultar.pack(pady=10)

root.mainloop()  