from Electrodomesticos import Electrodomesticos
from Lavadora import Lavadora
from Television import Television

almacen = ()
almacen = list(almacen)

almacen.insert(-1, Electrodomesticos(consumo_energético="A", peso=15))
almacen.insert(-1, Electrodomesticos(consumo_energético="B", peso=30))
almacen.insert(-1, Electrodomesticos(consumo_energético="C", peso=60))
almacen.insert(-1, Electrodomesticos(consumo_energético="D", peso=90))
almacen.insert(-1,Electrodomesticos(consumo_energético="A", peso=90))


almacen.insert(-1, Lavadora(consumo_energético="A", peso=50, carga=30))
almacen.insert(-1, Lavadora(consumo_energético="E", peso=50, carga=60))

almacen.insert(-1, Television(peso=20, resolucion=30))
almacen.insert(-1, Television(peso=20, resolucion=50))

tv = 0
lavadora = 0
cont = 0

for ele in almacen:

    if isinstance(ele, Television):
        tv += ele.precio_base
    elif isinstance(ele, Lavadora):
        lavadora += ele.precio_base
    else:
        cont += ele.precio_base

print("Total de televisores: " ,tv)
print("Total de lavadoras: " , lavadora)
print("Total de electrodomésticos: ", cont)

print("Total: ", (tv, lavadora, cont))