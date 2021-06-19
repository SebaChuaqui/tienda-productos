
class Tienda:

    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def __str__(self):
        return f"Tienda: {self.nombre}"

    def agregar_producto(self, nuevo_producto):
        self.productos.append(nuevo_producto)
        return self

    def eliminar_producto(self, id):
        print(f"Se elimina el producto: {self.id}")
        self.productos.pop(id)
        return self

    def inflacion(self, incremento_porcentual):
        for x in self.productos:
            x.actualizar_precio(incremento_porcentual/100)

    def descontar(self, categoria, descuento):
        for x in self.productos.categoria:
            x.actualizar_precio(descuento)

    def mostrar_productos(self):
        for x in self.productos:
            x.imprimir_info()

