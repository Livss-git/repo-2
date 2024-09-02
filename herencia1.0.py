class persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def presentarse(self):
        return f"soy{self.nombre}, tengo {self.edad}, años y soy de {self.nacionalidad}"
        
class artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidades (self):
        return f"mi habilidad es {self.habilidad}"
    
class escritor(persona, artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, libro):
        persona.__init__(self, nombre, edad, nacionalidad)
        artista.__init__(self, habilidad)
        self.libro = libro

    def escribir_novelas(self):
        return f"Escribo en libros como {self.libro}"
    
# crear objetos
escritor1 = escritor("juan", 45, "español", "escritura en prosa", "el amor en la oscurdad")

print(escritor1.presentarse())
print(escritor1.mostrar_habilidades())
print(escritor1.escribir_novelas())

