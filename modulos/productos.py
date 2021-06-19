class Productos:

    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria


        # Se imprime la informacion
    def __str__(self):
        imprimir = (f"Se agrega el producto: {self.nombre} cuyo valor es: ${self.precio} y se ubican en la categoria: {self.categoria}" )
        return imprimir

        # Se actualiza el precio
    def actualizar_precio(self, porcentaje_cambio, incrementa):
        if incrementa == True:
            print(f'el precio de {self.nombre} aumenta en {porcentaje_cambio}%')
            self.precio += (self.precio)*porcentaje_cambio/100
            print(f"precio final de {self.nombre} : {self.precio}")
            return self
        else:
            print(f'el precio de {self.nombre} disminuye en {porcentaje_cambio}%')
            self.precio -= (self.precio)*porcentaje_cambio/100
            print(f"precio final de {self.nombre} : {self.precio}")
            return self

    # Se cambia el precio 
    def nuevo_precio(self, nuevo_Precio):
        self.precio = nuevo_Precio
        return self
    # Se incrementa precio
    def incrementar(self, incremento):
        self.precio += self.precio * incremento/100
        print(f"El producto: {self.nombre} vale ahora ${self.precio}")
        return self






