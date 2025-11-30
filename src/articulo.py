class Articulo:
    # Modelo de un artículo del presupuesto
    def __init__(self, id, nombre, categoria, cantidad, precio_unit, descripcion):
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        self.cantidad = cantidad
        self.precio_unit = precio_unit
        self.descripcion = descripcion

    def total(self):
        return self.cantidad * self.precio_unit

    def a_dict(self):
        return self.__dict__

