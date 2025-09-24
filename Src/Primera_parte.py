def normalizar(texto):
    return texto.strip().lower()

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
    
def actualizar(inventario):
    producto_actualizar = input("\n¿A qué objeto desea actualizar su cantidad?: ").lower()
    for categoria, productos in inventario.items():
        for producto in productos:
            if producto["nombre"].lower() == producto_actualizar:

                try:
                    numero = int(input("Ingresar nueva cantidad: "))
                    producto["cantidad"] = numero
                    print("\nActualizado con éxito\n")
                    return 
                
                except ValueError:
                    print("\nFavor de escribir un número entero\n")
                    return 
    else:
        print("\nNo hay ningún producto con ese nombre")

def buscar_producto(inventario, busqueda):
    resultados = []
    for categoria, productos in inventario.items():
        for producto in productos:
            if busqueda.lower() in producto["nombre"].lower():
                resultados.append((categoria, producto))
    return resultados  

def eliminar_objeto(inventario):
    if not inventario:
        print("\n> No hay productos registrados.")
        return

    objeto_borrar = normalizar(input("Ingrese el nombre del producto a eliminar: "))
    for categoria, productos in inventario.items():
        for producto in productos:
            if normalizar(producto["nombre"]) == objeto_borrar:
                productos.remove(producto)
                print(f"Producto '{producto['nombre']}' eliminado de la categoría '{categoria}'.")
                return
    print("No se encontró el producto a eliminar.")

def menu():
    inventario = {}  

    while True:
        print("\n===== MENÚ DE INVENTARIO =====")
        print("1. Agregar productos")
        print("2. Mostrar inventario")
        print("3. Actualizar cantidad de un producto")
        print("4. Buscar producto")
        print("5. Eliminar producto")
        print("6. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            inventario = agregar_inventario()
        elif opcion == "2":
            if inventario:
                mostrar_inventario(inventario)
            else:
                print("Inventario vacío.")
        elif opcion == "3":
            if inventario:
                actualizar(inventario)
            else:
                print("Inventario vacío.")
        elif opcion == "4":
            if inventario:
                buscarP = input("Nombre del producto a buscar: ")
                encontrados = buscar_producto(inventario, buscarP)
                if encontrados:
                    print("Productos encontrados:")
                    for categoria, producto in encontrados:
                        print(f"- {producto['nombre']} | Cantidad: {producto['cantidad']} | Categoría: {categoria}")
                else:
                    print("No se encontró el producto")
            else:
                print("Inventario vacío.")
        elif opcion == "5":
            if inventario:
                eliminar_objeto(inventario)
            else:
                print("Inventario vacío.")
        elif opcion == "6":
            print("¡Gracias por usar nuestro porgrama!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
menu()