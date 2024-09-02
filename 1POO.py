# class nombreclase ():
#     atributo1=3
#     atributo2="pia"
#     atributo3=True

#     def saludar ():
#         print ("hola")

# objeto1 = nombreclase()
# print (objeto1.atributo2)
# objeto1.saludar()



class celular :
    def __init__(self , marca , modelo , camara ) :
        self.marca=marca 
        self.modelo=modelo
        self.camara=camara

        def llamar (self):
            print ("hola mundo")


celular1 = celular ("iphone" , "15 pro" , "90 mpx")
celular2 = celular ("samsung" , "s24" , "108 mpx")

print (f"Marca: {celular1.marca}")
print (f"Marca: {celular2.marca}")

# def llamar ():
#     print ("hola mundo")

celular1.llamar()





