def agregar_inventario():
    inventario = {}

    categorias = ["frios", "snacks", "enlatados", "limpieza", "mascotas", "calientes"]

    for categoria in categorias:
        try:
            cantidad = int(input(f"\n¿Cuántos productos de \"{categoria}\" quiere registrar?: "))
        except ValueError:
            cantidad = 0
        inventario[categoria] = []  

        if cantidad > 0:
            for i in range(cantidad):
                nombre = input("\nNombre del producto: ")
                try:
                    piezas = int(input("Cantidad en stock: "))
                except ValueError:
                    piezas = 0
                try:
                    minimo = int(input("¿Cantidad mínima para resurtido?: "))
                except ValueError:
                    minimo = 0
                inventario[categoria].append({
                    "nombre": nombre,
                    "cantidad": piezas,
                    "minimo": minimo
                })
                if piezas <= minimo:
                    print(f"AVISO: '{nombre}' tiene {piezas} unidades. Es necesario resurtir (mínimo {minimo}).")
                else:
                    print(f"'{nombre}' registrado con {piezas} unidades (mínimo {minimo}).")

            print("\n¡Sus productos fueron registrados exitosamente!")
    return inventario



def suma(inventario):
    categorias = ["frios", "snacks", "enlatados", "limpieza", "mascotas", "calientes"]
    
    for categoria in categorias:
        suma_total = 0
        for producto in inventario[categoria]:
            suma_total += producto["cantidad"]
        
        print("Categoria:", categoria)
        print("Suma total:", suma_total)
        
        productos = inventario[categoria]
        if len(productos) == 0:
            print("No hay productos registrados")
        else:
            for producto in productos:
                print(f"- {producto['nombre']}: {producto['cantidad']}")