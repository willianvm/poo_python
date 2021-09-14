
class Circulo:
    __pi = 3.14
    def __init__(self,radio):
        self.__radio = radio


    def __calcular_cuadrado_radio(self):
        return self.__radio ** 2

    def calcular_area(self):
        return self.__pi * self.__calcular_cuadrado_radio()
    
    #la sig funcion corresponde a un getter que te permite obtener el valor de un  atributo privado, que desde fuera de la clase no puedes observar
    def obtener_radio(self):
        return self.__radio
    
    # la sig funcion te permite cambiar el valor de un atributo privado, que desde fuera de la clase no hubieras podido cambiar
    def configurar_radio(self,radio):
        self.__radio = radio


circulo = Circulo(80)
print(f"el area del circulo es {circulo.calcular_area()}")

print(circulo.obtener_radio())
print(circulo.calcular_area())


circulo.configurar_radio(30)
print(circulo.obtener_radio())
print(circulo.calcular_area())

