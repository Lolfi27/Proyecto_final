#Se agregó input de actualizar precio y alerta de falta de stock
    
def actualizar(inventario):
    product_actualizar = input("\n¿Qué objeto desea actualizar?: ").lower().strip()

    # Se empiezan a recorrer las categorías
    for categoria, productos in inventario.items():
        for producto in productos:
            if producto["nombre"].lower() == product_actualizar:

                # ACTUALIZAR CANTIDAD
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

                # ACTUALIZAR PRECIO
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

                # Alerta de que se está quedando sin stock
                if producto["cantidad"] < producto["minimo"]:
                    print(f"   >> ALERTA: '{producto['nombre']}' tiene {producto['cantidad']} unidades "
                          f"(mínimo {producto['minimo']}).")

                return  # salir después de actualizar un producto

    
    print("\nNo hay ningún producto con ese nombre.")