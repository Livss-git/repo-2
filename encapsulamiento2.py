class persona:
    def __init__(self, name, apellido, nacionalidad):
        self.__name = name
        self.apellido = apellido
        self.nacionalidad = nacionalidad

    @property
    def datos (self):
        return self.__name

    @datos.setter
    def datos (self, values):
        self.__name = values
    
    
        
