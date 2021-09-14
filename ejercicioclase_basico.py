"""Cree una clase perro con los atributos raza, edad, color, nombre, que pueda ladrar, correr, dormir, comer, saltar. 
luego instanciela y imprima lo siguiente:
La raza del perro, y su comportamiento en determinado momento"""

class Perro:
    def __init__(self, raza, edad, color, nombre, velocidad):
        self.raza = raza
        self.edad = edad
        self.color = color
        self.nombre = nombre
        self.velocidad = velocidad

    def ladrar(self):
        print("el perro esta ladrando")

    def correr(self):
        print(f"Está corriendo a una velocidad de {self.velocidad} m/s  y luego"), self.ladrar()

    def dormir(self):
        print("el perro esta dormido")

perro1 = Perro("pincher",3, "negro", "roky", 3)


print(f"El perro es {perro1.raza} y"), perro1.correr()
