class x:
    def __init__(self, a, b):
        self.__a = a 
        self.b = b 
    
    def get_a(self):
        return self.__a 
    
    def set_a (self, aa):
        self.__a = aa

    def __saludo (self):
        pass

        
x1 = x(3, "hola")
print (x1.get_a())
x1.set_a(23)
print (x1.get_a())





