from gestor import GestorArticulos

gestor = GestorArticulos()

def mostrar_tabla(lista):
    # Muestra la lista de artículos en formato alineado
    print(f"{'ID':<5}{'Nombre':<15}{'Categoria':<15}{'Cant':<6}{'P/U':<10}{'Total':<10}")
    print("-" * 62)
    for a in lista:
        print(f"{a.id:<5}{a.nombre:<15}{a.categoria:<15}{a.cantidad:<6}{a.precio_unit:<10.2f}{a.total():<10.2f}")

while True:
    print("\n1. Registrar\n2. Buscar por nombre\n3. Buscar por categoria\n4. Editar\n5. Eliminar por ID\n6. Listar\n7. Salir")
    op = input("Opcion: ")

    if op == "1":
        gestor.registrar(
            input("Nombre: "),
            input("Categoria: "),
            int(input("Cantidad: ")),
            float(input("Precio unitario: ")),
            input("Descripcion: ")
        )

    elif op == "2":
        mostrar_tabla(gestor.buscar(input("Buscar: "), "nombre"))

    elif op == "3":
        mostrar_tabla(gestor.buscar(input("Buscar: "), "categoria"))

    elif op == "4":
        id = int(input("ID a editar: "))
        gestor.editar(id,
            cantidad=int(input("Nueva cantidad: ")),
            precio_unit=float(input("Nuevo precio unitario: "))
        )

    elif op == "5":
        gestor.eliminar(input("ID a eliminar: "), "id")

    elif op == "6":
        mostrar_tabla(gestor.listar())

    elif op == "7":
        break
