import json
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
    product_actualizar = input("\n¿Qué objeto desea actualizar?: ").lower().strip()

    for categoria, productos in inventario.items():
        for producto in productos:
            if producto["nombre"].lower() == product_actualizar:

                while True:
                    numero = input("¿Desea actualizar su cantidad? (s/n): ").lower().strip()
                    if numero == "s":
                        try:
                            nuevo_numero = int(input("Ingresar nueva cantidad: "))
                            producto["cantidad"] = nuevo_numero
                            print("\nActualizado con éxito.\n")
                        except ValueError:
                            print("Favor de escribir un número entero")
                        
                        break
                    elif numero == "n":
                        print("No hay ninguna cantidad por actualizar")
                        break
                    else:
                        print("Respuesta no válida, favor de escribir 's' o 'n'.")

                while True:
                    precio = input("¿Desea actualizar el precio? (s/n): ").lower().strip()
                    if precio == "s":
                        try:
                            nuevo_precio = float(input("Ingresar nuevo precio: "))
                            producto["precio"] = nuevo_precio
                            print("Precio actualizado con éxito.")
                        except ValueError:
                            print("Favor de escribir solamente el número")
                        break
                    elif precio == "n":
                        print("No hay ningún precio por actualizar...!")
                        break
                    else:
                        print("Respuesta no válida, favor de escribir 's' o 'n'.")

                if producto["cantidad"] < producto["minimo"]:
                    print(f"   >> ALERTA: '{producto['nombre']}' tiene {producto['cantidad']} unidades "
                          f"(mínimo {producto['minimo']}).")

                return

    
    print("\nNo hay ningún producto con ese nombre.")

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

def creador_de_archivo(nombre_archivo=""): 
    if nombre_archivo == "":
        nombre_archivo = input("Cual es el nombre del archivo?\n").strip()
        if nombre_archivo == "":
            nombre_archivo = "inventario"   
    archivo = f"{nombre_archivo}.txt"
    try:
        with open(archivo, "x", encoding="utf-8") as file:
            pass
        print(f"Archivo '{archivo}' creado con exito.")
    except FileExistsError:
        print(f"Archivo {archivo} ya existe")
        modificar = input("Desea modifica el contenido del archivo? (s/n)\n").strip().lower()
        if modificar != "s":
            sobreescribir = input("Desea sobrescribir el archivo? (s/n)\n").strip().lower()
            if sobreescribir == "s":
                with open(archivo, "w", encoding="utf-8") as file:
                    pass
                print(f"Archivo {archivo} sobreescrito.")
            else:
                print(f"Archivo {archivo} sin cambios")
    return archivo

def guardar_inventario(inventario, nombre_archivo):
    with open(nombre_archivo.replace(".txt",".json"),"w",encoding="utf-8")as file:
        json.dump(inventario,file,indent=4,ensure_ascii=False)
    
    with open(nombre_archivo, "w", encoding="utf-8") as file:
        for categoria,productos in inventario.items():
            file.write(f"\n==== {categoria.upper()} ====\n")
            if not productos:
                file.write("No hay productos en existencia\n")
            for producto in productos:
                file.write(f"Nombre: {producto['nombre']}\n Cantidad: {producto['cantidad']}\n Precio: ${producto['precio']}\nMínimo: {producto['minimo']}\n-------------\n")


def cargar_inventario(nombre_archivo):
    try:
        with open(nombre_archivo.replace(".txt",".json"),"r",encoding="utf-8")as file:
            return json.load(file)          
    except (FileNotFoundError, json.JSONDecodeError):
        return inventario_vacio()

def inventario_vacio():
    return {"frios": [], "snacks": [], "enlatados": [], "limpieza": [], "mascotas": [], "calientes": []}

archivo_inventario = creador_de_archivo()
inventario = cargar_inventario(archivo_inventario)

def menu():
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
            guardar_inventario(inventario,archivo_inventario)
        elif opcion == "2":
            inventario = cargar_inventario(archivo_inventario)
            if inventario:
                mostrar_inventario(inventario)
            else:
                print("Inventario vacío.")
        elif opcion == "3":
            inventario = cargar_inventario(archivo_inventario)
            if inventario:
                actualizar(inventario)
                guardar_inventario(inventario,archivo_inventario)
        elif opcion == "4":
            inventario = cargar_inventario(archivo_inventario)
            if inventario:
                buscarP = input("Nombre del producto a buscar: ")
                encontrados = buscar_producto(inventario, buscarP)
                if encontrados:
                    print("Productos encontrados:")
                    for categoria, producto in encontrados:
                        print(f"- {producto['nombre']} | Cantidad: {producto['cantidad']} | Categoría: {categoria}")
                else:
                    print("No se encontró el producto")
        elif opcion == "5":
            inventario = cargar_inventario(archivo_inventario)
            if inventario:
                eliminar_objeto(inventario)
                guardar_inventario(inventario, archivo_inventario)
        elif opcion == "6":
            if not inventario:
                inventario = inventario_vacio()
                guardar_inventario(inventario, archivo_inventario)
                print("¡Gracias por usar nuestro programa!")
                break
            else:
                guardar_inventario(inventario, archivo_inventario)
                print("¡Gracias por usar nuestro programa!")
                break
        else:
            print("Opción no válida. Intente de nuevo.")
menu()