import json
import os
from articulo import Articulo

DATA_FILE = "../data/articulos.json"

class GestorArticulos:
    # Maneja operaciones CRUD y persistencia en JSON
    def __init__(self):
        self.articulos = []
        self._cargar()

    def _cargar(self):
        if not os.path.exists(DATA_FILE):
            os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
            with open(DATA_FILE, "w") as f:
                json.dump([], f)
        with open(DATA_FILE, "r") as f:
            datos = json.load(f)
            self.articulos = [
                Articulo(**item) for item in datos
            ]

    def _guardar(self):
        with open(DATA_FILE, "w") as f:
            json.dump([a.a_dict() for a in self.articulos], f, indent=2)

    def registrar(self, nombre, categoria, cantidad, precio_unit, descripcion):
        nuevo_id = len(self.articulos) + 1
        articulo = Articulo(nuevo_id, nombre, categoria, cantidad, precio_unit, descripcion)
        self.articulos.append(articulo)
        self._guardar()

    def buscar(self, criterio, campo="nombre"):
        return [
            a for a in self.articulos
            if criterio.lower() in getattr(a, campo).lower()
        ]

    def editar(self, id, **campos):
        for a in self.articulos:
            if a.id == id:
                for key, value in campos.items():
                    setattr(a, key, value)
                self._guardar()
                return True
        return False

    def eliminar(self, criterio, campo="id"):
        self.articulos = [
            a for a in self.articulos
            if criterio.lower() not in str(getattr(a, campo)).lower()
        ]
        self._guardar()

    def listar(self):
        return self.articulos
