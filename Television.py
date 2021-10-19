from Electrodomesticos import Electrodomesticos


class Television(Electrodomesticos):

    def __init__(self, precio_base=100, color="blanco", consumo_energético='F', peso=5, resolucion=20, fourK=False):
        Electrodomesticos.__init__(self, precio_base=precio_base, color=color, consumo_energético=consumo_energético, peso=peso)
        self.resolucion = resolucion
        self.fourK = fourK

    def precioFinal(self):
        Electrodomesticos.precioFinal(self)
        if self.resolucion > 40:
            self.precio_base = self.precio_base * 1.3
        if self.fourK == True:
            self.precio_base = self.precio_base + 50

    def getResolucion(self,resolucion):
        self.resolucion = resolucion

    def getFourk(self,fourK):
        self.fourK = fourK