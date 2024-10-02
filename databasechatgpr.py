import tkinter as tk
from tkinter import messagebox
import psycopg2

def conectar_db():
    try:
        conn = psycopg2.connect(
            dbname="conectar",
            user="postgres",
            password="livan123",
            host="localhost",
            port="5432"
        )
        print("conexión exitosa")
        return conn
    except psycopg2.Error as e:
        messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {e}")
        exit()

def agregar_ventana():
    id = entry_id.get()
    nombre = entry_nombre.get()
    venta = entry_venta.get()
    sucursal = entry_sucursal.get()

    if nombre and venta and sucursal:
        try:
            conn = conectar_db()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO venta (id, nombre, venta, sucursal) VALUES (%s, %s, %s, %s)", (id, nombre, venta, sucursal))
            conn.commit()
            messagebox.showinfo("Éxito", "Venta registrada correctamente")
            limpiar_formulario()
        except psycopg2.Error as e:
            messagebox.showerror("Error", f"No se pudo registrar la venta: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        messagebox.showerror("Error", "Todos los campos son obligatorios")

def limpiar_formulario():
    entry_id.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_venta.delete(0, tk.END)
    entry_sucursal.delete(0, tk.END)

def abrir_ventana_consulta():
    consulta_ventana = tk.Toplevel(root)
    consulta_ventana.title("Consulta")
    consulta_ventana.geometry("300x200")
    
    tk.Label(consulta_ventana, text="Ingrese el ID").pack(pady=10)
    entry_id_consulta = tk.Entry(consulta_ventana)
    entry_id_consulta.pack()

    # Cambiamos aquí para llamar a la función directamente
    tk.Button(consulta_ventana, text="Consultar", command=lambda: consultar(entry_id_consulta)).pack(pady=10)

def consultar(entry_id_consulta):
    id_consulta = entry_id_consulta.get()
    if id_consulta:
        try:
            conn = conectar_db()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM venta WHERE id=%s", (id_consulta,))
            row = cursor.fetchone()
            if row:
                messagebox.showinfo("Resultado", f"ID: {row[0]}, Nombre: {row[1]}, Venta: {row[2]}, Sucursal: {row[3]}")
            else:
                messagebox.showinfo("Resultado", "No se encontró el ID")
        except psycopg2.Error as e:
            messagebox.showerror("Error", f"No se pudo consultar la venta: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        messagebox.showerror("Error", "El ID es obligatorio")

def actualizar_venta():
    id_actualizar = entry_id.get()
    nombre_actualizar = entry_nombre.get()
    venta_actualizar = entry_venta.get()
    sucursal_actualizar = entry_sucursal.get()
    
    if nombre_actualizar and venta_actualizar and sucursal_actualizar:
        try:
            conn = conectar_db()
            cursor = conn.cursor()
            cursor.execute("UPDATE venta SET nombre=%s, venta=%s, sucursal=%s WHERE id=%s", (nombre_actualizar, venta_actualizar, sucursal_actualizar, id_actualizar))
            conn.commit()
            messagebox.showinfo("Éxito", "Venta actualizada correctamente")
            limpiar_formulario()
        except psycopg2.Error as e:
            messagebox.showerror("Error", f"No se pudo actualizar la venta: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        messagebox.showerror("Error", "Todos los campos son obligatorios")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Registro de ventas")
root.geometry("300x300")

tk.Label(root, text="ID").pack(pady=10)
entry_id = tk.Entry(root)
entry_id.pack()

tk.Label(root, text="Nombre").pack(pady=10)
entry_nombre = tk.Entry(root)
entry_nombre.pack()

tk.Label(root, text="Venta").pack(pady=10)
entry_venta = tk.Entry(root)
entry_venta.pack()

tk.Label(root, text="Sucursal").pack(pady=10)
entry_sucursal = tk.Entry(root)
entry_sucursal.pack()

# Botones
agregar_boton = tk.Button(root, text="Agregar", command=agregar_ventana)
agregar_boton.pack(pady=10)

limpiar_boton = tk.Button(root, text="Limpiar", command=limpiar_formulario)
limpiar_boton.pack(pady=10)

consulta_boton = tk.Button(root, text="Consultar", command=abrir_ventana_consulta)
consulta_boton.pack(pady=10)

actualizar_boton = tk.Button(root, text="Actualizar", command=actualizar_venta)
actualizar_boton.pack(pady=10)

root.mainloop()