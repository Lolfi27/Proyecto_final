# Preguntar si se modificara un inventario ya existente o se creara uno nuevo
inventario=[]
#####################################################
# ===== Utilidades =====
def normalizar(texto):
    return texto.strip().lower()

def eliminar_objeto():
    if not inventario:
        print("\n> No hay objetos registrados.")
        return

    objeto_borrar = normalizar(input("Ingrese objeto "))
    for objeto in inventario:
        if normalizar(objeto["Objeto"]) == objeto_borrar:
            inventario.remove(objeto)
            print("Objeto eliminado.")
            return

# Ingresar la cantidad total de objetos:
objetos_a_registrar = int(input("Cuantos objetos se van a registrar"))
# Variables de input
objetos_frios = int(input("Cuantos objetos almacenados en frio habra?"))
objetos_snacks = int(input("Cuantas chucherias habra?"))
objetos_enlatados = int(input("Cuantos enlatados habra?"))
objetos_limpieza = int(input("Cuantos objetos de limpieza habra?"))
objetos_mascotas = int(input("Cuantos objetos de mascotas habra?"))
objetos_calientes = int(input("Cuantos objetos calientes habra?"))

# Aqui se ponen otras variables

# Sistema de separación y conteo individual por tipo de objeto
# Aqui se separa cada objeto de cada categoria para un control más preciso
# ej. "Cuantas papas habra?" Registrado como 1 interger de objetos_snacks

# Conexión de datos a text file para un manejo de codigo
# Si hay datos ya existentes, se sobrescribiran con las modificaciones permitidas

# Al finalizar, se pregunta si el usuario hara algun cambio diferente

