class Figura:
    def calcular_area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * self.radio**2

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

circulo = Circulo(5)
rectangulo = Rectangulo(4, 6)

print("Área del círculo:", circulo.calcular_area())  # Imprime el área del círculo
print("Área del rectángulo:", rectangulo.calcular_area())  # Imprime el área del rectángulo
