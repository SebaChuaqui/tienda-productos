class Productos:

    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

        # Se imprime la informacion
    def imprimir_info(self):
        print(f"""
                PRODUCTO
                nombre: {self.nombre}
                precio: {self.precio}
                categoria: {self.categoria}
                """)
        return self

    # Se cambia el precio 
    def nuevo_precio(self, nuevo_Precio):
        self.precio = nuevo_Precio
        return self
    # Se incrementa precio
    def incrementar(self, incremento):
        self.precio += self.precio * incremento/100
        print(f" El producto: {self.nombre} vale ahora {self.precio}")
        return self




    

    






