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
#VERIFICAR DÍA
            while True:
                try:
                    d = int(input("Día de registro del producto (1-31): "))
                    if 1 <= d <= 31:
                        return d
                    else:
                        print("El dia tiene que estar entre 1-31")
                except ValueError:
                    print("Por favor, ingrese solo numeros enteros")
#VERIFICAR MES
            while True:
                try:
                    m = int(input("Mes de registro del producto (1-12): "))
                    if 1 <= m <= 12:
                        return m
                    else:
                        print("El mes tiene que estar entre 1 y 12")
                except ValueError:
                    print("Por favor, ingrese solo numeros enteros")
#VERIFICAR AÑO
            while True:
                try:
                    a = int(input("Año de registro del producto: "))
                    if a > 0:
                        return a
                    else:
                        print("El año tiene que ser mayor a 0")
                except ValueError:
                    print("Por favor, ingrese solo numeros enteros")
                
            inventario[categoria].append({"nombre": nombre, "cantidad": piezas, "fecha": (d, m, a)})
            print("\n¡Sus productos fueron registrados exitosamente!")
    return inventario
