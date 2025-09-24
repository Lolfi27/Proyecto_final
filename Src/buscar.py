def buscar_producto(busqueda):
    resultados = []
    inventario = []
    for producto in inventario:
        if busqueda.lower() in producto["nombre"].lower():
            resultados.append(producto)
    return resultados  


while True:
    buscarP = input("Nombre del producto a buscar (o 'salir' para terminar): ")
    if buscarP.lower() == "salir":  
        print("Saliendo del buscador...")
        break

    encontrados = buscar_producto(buscarP)
    if encontrados:
        print("Productos encontrados:")
        for producto in encontrados:
            print(f"- {producto['nombre']} | Cantidad: {producto['cantidad']} | Fecha: {producto['fecha']['dia']}/{producto['fecha']['mes']}/{producto['fecha']['año']}")
    else:
        print("No se encontró el producto")


