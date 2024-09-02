class persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

class empleado:
    def __init__(self, salario, area):
        self.__salario = salario
        self.__area = area


class vendedor(empleado):
    def __init__(self, salario, area, ventas):
        empleado.__init__(salario, area)
        self.__ventas = ventas

        



