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
                try:
                    precio = float(input("Precio del producto: $"))
                except ValueError:
                    precio = 0.0

                inventario[categoria].append({
                    "nombre": nombre,
                    "cantidad": piezas,
                    "minimo": minimo,
                    "precio": precio
                })

            print("\n¡Sus productos fueron registrados exitosamente!")
    return inventario


def mostrar_inventario(inventario):  
    categorias = ["frios", "snacks", "enlatados", "limpieza", "mascotas", "calientes"]
    
    for categoria in categorias:
        suma_total = 0
        print(f"\nCategoría: {categoria}")
        
        productos = inventario[categoria]
        if len(productos) == 0:
            print("No hay productos registrados")
        else:
            for producto in productos:
                suma_total += producto["cantidad"]
                print(f"- {producto['nombre']} | Cantidad: {producto['cantidad']} | "
                      f"Precio: ${producto['precio']:.2f} | Mínimo: {producto['minimo']}")
                
                if producto["cantidad"] < producto["minimo"]:
                    print(f"   >> ALERTA: '{producto['nombre']}' tiene {producto['cantidad']} unidades "
                          f"(mínimo {producto['minimo']}).")

        print(f"Total de piezas en categoría '{categoria}': {suma_total}")
    