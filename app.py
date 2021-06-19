from modulos.tienda import Tienda
from modulos.productos import Productos

tienda1 = Tienda("Asereje")
print(tienda1)

tienda2 = Tienda("La Mamorta")
print(tienda2)

producto1 = Productos(1, "Yogurt Natural", 345, "Lacteos")
tienda1.agregar_producto(producto1)
print(producto1)
producto1.actualizar_precio(4,5)

producto2= Productos(2, "Beterraga", 890, "Verduras")
tienda1.agregar_producto(producto2)
print(producto2)
producto2.incrementar(20)

producto3= Productos(3, "Papas Fritas", 1490, "Snack")
tienda1.agregar_producto(producto3)
print(producto3)
producto3.incrementar(50)
producto3.actualizar_precio(3, 10)




