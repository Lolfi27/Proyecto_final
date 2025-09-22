def agregar_inventario():
    inventario = {}

    categorias = ["frios", "snacks", "enlatados", "limpieza", "mascotas", "calientes"]

    for categoria in categorias:
        try:
            cantidad = int(input("\nCuantos productos de " + categoria + " quiere registrar: "))
        except ValueError:
            cantidad = 0
        inventario[categoria] = []  
        for i in range(cantidad):
            nombre = input("\nNombre del producto:")
            try:
                piezas = int(input("Cantidad: "))
            except ValueError:
                piezas = 0
            inventario[categoria].append({"nombre": nombre, "cantidad": piezas})
            print("\n¡Sus productos fueron registrados exitosamente!")
    return inventario

