"""definir una clase lavadora con nombre, modelo y año que llena, lava, enjuaga y centrifuga
  y encapsule los métodos de esta"""

class Lavadora:
    def __init__(self, nombre, modelo, año):
        self.nombre = nombre
        self.modelo = modelo
        self.año = año

    def __llenar(sel):
        print("la labadora esta llenando")
    
    def lavar(self):
        print("lavando!!!")

    def __enjuagar(self):
        print("enjuagando!!!!")

    def __centrifugar(self):
        print("centrifugando!!")

class Lavaplatos(Lavadora):
    def __init__(self, nombre, modelo, año, vencimiento):
        super().__init__(nombre,modelo,año)
        self.vencimiento = vencimiento
    
    def lavar(self):
        print("El lavaplatos esta lavando la losa")

lavadora = Lavadora("wilpoor", "zx123", 2015)  
lavadora.lavar()
lavaplatos = Lavaplatos("corona", "zx", 2016, 2030)
lavaplatos.lavar()


