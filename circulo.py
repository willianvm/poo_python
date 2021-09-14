""""Cree una clase circulo que a partir de un radio calcule el cuadrado y el area del circulo"""

class Circulo:
    pi = 3.14
    def __init__(self,radio):
        self.radio = radio


    def calcular_cuadrado_radio(self):
        return self.radio ** 2

    def calcular_area(self):
        return self.pi * self.calcular_cuadrado_radio()

circulo = Circulo(80)
print(f"el area del circulo es {circulo.calcular_area()}")

circulo.radio = 30
print(f"el area del circulo es {circulo.calcular_area()}")