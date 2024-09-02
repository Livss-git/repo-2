class persona:
    def __init__(self, nombre , edad , nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad 

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años. Soy de {self.nacionalidad}.")

class estudiante(persona):
    def __init__(self, nombre, edad, nacionalidad, carrera, n1, n2, n3):
        super().__init__(nombre, edad, nacionalidad)
        self.carrera = carrera
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def promedio(self):
        return (self.n1 + self.n2 + self.n3) / 3
    
estudiante1 = estudiante("tiburcio", 46, "camboya", "ing software", 4, 5, 3)
estudiante1.saludar()
promedio = estudiante1.promedio()
print(f"El promedio de los tres notas es: {promedio}")


# class x:
#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def saludar(self):
#         print ("hola saludar")

# # lalas = x(2,"hola" , 12)
# # lalas.saludar()

# class y(x):
#     def __init__(self,a,b,c,s,t):
#         super().__init__(a,b,c)
#         self.s = s
#         self.t = t


# yx = y (1,2,3,"luz","liz")
# yx.saludar()







