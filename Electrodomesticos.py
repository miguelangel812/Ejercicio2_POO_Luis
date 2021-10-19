class Electrodomesticos():
    precio_base = 100
    color = "Blanco"
    consumo_energético = "F"
    peso = 5


    def __init__(self, precio_base=100,color="blanco",consumo_energético='F',peso=5):
        if color in ("blanco", "negro", "rojo", "azul" , "gris"):
            self.color=color
        self.precio_base = precio_base
        self.comprobarConsumoEnergetico(consumo_energético)
        self.peso = peso

    def comprobarConsumoEnergetico(self,consumo_energético):
        if consumo_energético in ("A","B","C","D","E","F"):
            self.consumo_energético = consumo_energético
        else:
            self.consumo_energético = "F"

        return self.consumo_energético


    def precioFinal(self):
        if (self.consumo_energético == "A"):
            self.precio_base = self.precio_base + 100
        if (self.consumo_energético == "B"):
            self.precio_base = self.precio_base + 80
        if (self.consumo_energético == "C"):
            self.precio_base = self.precio_base + 60
        if (self.consumo_energético == "D"):
            self.precio_base = self.precio_base + 50
        if (self.consumo_energético == "E"):
            self.precio_base = self.precio_base + 30
        if (self.consumo_energético == "F"):
            self.precio_base = self.precio_base + 10


        if(self.peso > 0 and self.peso < 19):
            self.precio_base = self.precio_base + 10
        if (self.peso > 20 and self.peso < 49):
            self.precio_base = self.precio_base + 50
        if (self.peso > 50 and self.peso < 79):
            self.precio_base = self.precio_base + 80
        if (self.peso > 80):
            self.precio_base = self.precio_base + 100



    def getNombre(self,precio_base):
        self.precio_base = precio_base
    def getColor(self,color):
        self.color = color
    def getConsumo_energetico(self,consumo_energético):
        self.consumo_energético = consumo_energético
    def getPeso(self,peso):
        self.peso = peso

