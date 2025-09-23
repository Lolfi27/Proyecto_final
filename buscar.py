inventario = []
def buscar_producto(busqueda):
    resultados = []
    for producto in inventario:
        if busqueda.lower() in producto["nombre"].lower():
            resultados.append(producto)
        return resultados
    
while True:
        buscarP  = input("Nombre del producto a buscar: ")
        if buscarP.lower() == "Salir":
            print("Saliendo del buscador...")
            break

        encontrados = buscar_producto(buscarP)
        if encontrados:
            print("Producto encontrado: ")
            if p in encontrados:
               print(f"- {p{'nombre'}} | Precio: ${p['precio']}")
        else:
            print("No se encontro  el producto")
        
