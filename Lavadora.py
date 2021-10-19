
from Electrodomesticos import Electrodomesticos

class Lavadora(Electrodomesticos):

    def __init__(self, precio_base=100, color="blanco", consumo_energético='F', peso=5, carga=5):
        Electrodomesticos.__init__(self, precio_base=precio_base, color=color, consumo_energético=consumo_energético, peso=peso)
        self.carga=carga

    def precioFinal(self):
        Electrodomesticos.precio_base(self)
        if self.carga > 30:
            self.precio_base = self.precio_base + 50

    def getCarga(self,carga):
        self.carga = carga