class persona:
    def __init__(self, nombre, edad,):
        self.nombre = nombre
        self.edad = edad

class empleado(persona):
    def __init__(self, nombre, edad, salario, area):
        self.salario = salario
        self.area = area
        super().__init__(nombre, edad)

class cliente(persona):
    def __init__(self, nombre, edad, compra, bono):
        self.compra = compra
        self.bono = bono
        super().__init__(nombre, edad)


class vendedor(empleado):
    def __init__(self, nombre, edad, salario, area, venta, sucursal):
        super().__init__(nombre, edad, salario, area)
        self.venta = venta
        self.sucursal = sucursal

    
    def calcula_com(self):
        return self.venta * 0.11 

p1 = persona("Juan", 30)
e1 = empleado("Ana", 40, 2000, "Contabilidad")
c1 = cliente("Maria", 25, 1000, 500)
v1 = vendedor("Pedro", 35, 3000, "Ventas", 5000, "Sucursal A")

print(f"Nombre: {p1.nombre}, Edad: {p1.edad}")

print(f"Nombre: {e1.nombre}, Edad: {e1.edad}, Salario: {e1.salario}, Area: {e1.area}")

print(f"Nombre: {c1.nombre}, Edad: {c1.edad}, Compra: {c1.compra}, Bono: {c1.bono}")

print(f"Nombre: {v1.nombre}, Edad: {v1.edad}, Salario: {v1.salario}, Area: {v1.area}, Venta: {v1.venta}, Sucursal: {v1.sucursal}, Comision: {v1.calcula_com()}")



