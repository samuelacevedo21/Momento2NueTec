class Producto:
    def __init__(self, id, nombre, descripcion, costo, cantidad, margen_de_venta):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.cantidad = cantidad
        self.margen_de_venta = margen_de_venta
        self.precio_de_venta = None

    def calcular_precio_de_venta(self):
        if self.margen_de_venta <= 0 or self.costo <= 0:
            raise ValueError("Margen de venta y costo deben ser mayores que cero")
        self.precio_de_venta = self.costo / (1 - self.margen_de_venta)

class Inventario:
    def __init__(self):
        self.productos = {}

    def registrar_producto(self, id, nombre, descripcion, costo, cantidad, margen_de_venta):
        if id in self.productos:
            raise ValueError(f"El producto con ID {id} ya existe en el inventario.")
        producto = Producto(id, nombre, descripcion, costo, cantidad, margen_de_venta)
        producto.calcular_precio_de_venta()
        self.productos[id] = producto

    def imprimir_lista_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Listado de Productos:")
            for producto_id, producto in self.productos.items():
                print(f"ID: {producto_id}, Nombre: {producto.nombre}, Precio de Venta: {producto.precio_de_venta}")

# Ejemplo de uso
if __name__ == "__main__":
    inventario = Inventario()

    while True:
        try:
            id = int(input("Ingrese el ID del producto (0 para salir): "))
            if id == 0:
                break
            nombre = input("Nombre del producto: ")
            descripcion = input("Descripción del producto: ")
            costo = float(input("Costo del producto: "))
            cantidad = int(input("Cantidad del producto: "))
            margen_de_venta = float(input("Margen de venta (porcentaje): ")) / 100

            inventario.registrar_producto(id, nombre, descripcion, costo, cantidad, margen_de_venta)
        except ValueError as e:
            print(f"Error: {e}")

    inventario.imprimir_lista_productos()
