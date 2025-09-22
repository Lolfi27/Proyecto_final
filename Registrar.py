def agregar_inventario():
    try:
        productos_a_registrar = int(input("\n¿Cuántos productos desea registrar?: "))
    except ValueError:
        print("Favor de escribir un número entero")
        agregar_inventario()

    while productos_a_registrar > 0:
        #LLENAR DATOS
        print("Favor de llenar los datos  requeridos:")

        nombre_producto = input("\nNombre del producto: ").strip()
        while True:
            try:
                cantidad_producto = int(input("Cantidad del producto: "))
                break
            except ValueError:
                print("Favor de escribir un número entero")
                
        
        verificar_dia()
        verificar_año()
        verificar_mes()
        
        # BIBLIOTECA

        print("¡¡¡Producto/s agregado/s con éxito!!!")
        productos_a_registrar -= 1

    else:
        print("No hay nada por agregar.")




# DÍA / MES / AÑO

def verificar_dia():
    while True:
        try:
            d = int(input("Día de registro del producto (1-31): "))
            if 1 <= d <= 31:
                return d
            else:
                print("El dia tiene que estar entre 1-31")
        except ValueError:
            print("Por favor, ingrese solo numeros enteros")
def verificar_mes():
    while True:
        try:
            m = int(input("Mes de registro del producto (1-12): "))
            if 1 <= m <= 12:
                return m
            else:
                print("El mes tiene que estar entre 1 y 12")
        except ValueError:
            print("Por favor, ingrese solo numeros enteros")
def verificar_año():
    while True:
        try:
            a = int(input("Año de registro del producto: "))
            if a > 0:
                return a
            else:
                print("El año tiene que ser mayor a 0")
        except ValueError:
            print("Por favor, ingrese solo numeros enteros")