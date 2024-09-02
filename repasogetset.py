class persona :
    def __init__(self, nombre, edad, nacionalidad):
        self.__nombre = nombre
        self.__edad = edad
        self.nacionalidad = nacionalidad

    # def get_nombre(self):
    #     return self.__nombre

class cliente (persona) : 
    def __init__(self, nombre, edad, nacionalidad, compra, descuento):
        super().__init__(nombre, edad, nacionalidad)
        self.__compra = compra
        self.__descuento = descuento

# acceder a archivos encapsulados
    def get_descuento (self) : 
        return self.__descuento
    
# cambia archivos encapsulados    
    def set_descuento (self, nuevo_descuento) :
        self.__descuento = nuevo_descuento

cliente1 = cliente ("libia", 34, "argentina", 200, 0.1)
# print (f"el nombre del cliente es : {cliente1.get_nombre()}")
cliente1.set_descuento(0.2)
print (f"el descuento es : {cliente1.get_descuento()}")