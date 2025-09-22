def agregar_inventario():
    inventario = {}

    categorias = ["frios", "snacks", "enlatados", "limpieza", "mascotas", "calientes"]

    for categoria in categorias:
        try:
            cantidad = int(input(f"\nCuantos productos de \"{categoria}\" quiere registrar: "))
        except ValueError:
            cantidad = 0
        inventario[categoria] = []  
        if cantidad > 0:
            for i in range(cantidad):
                nombre = input("\nNombre del producto: ")
                try:
                    piezas = int(input("Cantidad: "))
                except ValueError:
                    piezas = 0
                inventario[categoria].append({"nombre": nombre, "cantidad": piezas})
            print("\n¡Sus productos fueron registrados exitosamente!")
    return inventario

def suma_por_categoria(inventario):
    suma_total = {}
    categorias = ["frios", "snacks", "enlatados", "limpieza", "mascotas", "calientes"]
    for categoria in categorias:
        suma = 0
        for producto in inventario[categoria]:
            suma += producto["cantidad"]
        suma_total[categoria] = suma
    return suma_total
