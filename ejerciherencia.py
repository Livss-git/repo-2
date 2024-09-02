class persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

class empleado:
    def __init__(self, salario, sucursal):
        self.salario = salario
        self.sucursal = sucursal

class planta(persona, empleado):
    def __init__(self, nombre, edad, nacionalidad, salario, sucursal, bono, saldo_h_extras, desc_seguridad):
        persona.__init__(self, nombre, edad, nacionalidad)
        empleado.__init__(self, salario, sucursal)
        self.bono = bono
        self.saldo_h_extras = saldo_h_extras
        self.desc_seguridad = desc_seguridad

    def sueldo(self):
        return self.salario + self.bono + self.saldo_h_extras - self.desc_seguridad

class contratista(persona, empleado):
    def __init__(self, nombre, edad, nacionalidad, salario, sucursal, retefuente):
        persona.__init__(self, nombre, edad, nacionalidad)
        empleado.__init__(self, salario, sucursal)
        self.retefuente = retefuente

    def sulcontra (self):
        return self.salario - self.retefuente

empleadop1 = planta ("livss", 17, "colombiano", 8500, "sucursal_H", 300, 400, 100 )
print (f"el sueldo del empleado de platnta es {empleadop1.sueldo()}")

contratista1 = contratista ("jose", 30, "colombiano", 4000, "sucursal_A", (4000*0.03))
print (f"el sueldo del contratista es {contratista1.sulcontra()}")

# Livan David Silvera Albarrcin

