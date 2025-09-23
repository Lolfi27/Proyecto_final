#EDITAR INVENTARIO
def actualizar(inventario):
    product_actualizar = input("\n¿A qué objeto desea actualizar su cantidad?: ")

#Se empiezan a recorrer las categorías
    for categoria, productos in inventario.items():
        for producto in productos:
            if producto["nombre"].lower() == product_actualizar:

                try:
                    numero = int(input("Ingresar nueva cantidad: "))
                    producto["cantidad"] = numero
                    print("\nActualizado con éxito\n")
                    return  #salir después de actualizar
                
                except ValueError:
                    print("\nFavor de escribir un número entero\n")
                    return #salir si hay un error
    else:
        print("\nNo hay ningún producto con ese nombre")
