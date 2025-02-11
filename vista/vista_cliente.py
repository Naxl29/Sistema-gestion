def mostrar_menu():
    print("\n--- Menú Cliente ---")
    print("1. Crear Cliente")
    print("2. Mostrar Clientes")
    print("3. Eliminar Cliente")
    print("4. Actualizar Cliente")
    print("5. Salir")

def obtener_datos_cliente():
    pri_nombre = input("Ingrese el primer nombre: ")
    seg_nombre = input("Ingrese el segundo nombre (puede dejarlo vacío): ")
    pri_apellido = input("Ingrese el primer apellido: ")
    seg_apellido = input("Ingrese el segundo apellido (puede dejarlo vacío): ")
    documento = input("Ingrese el documento (número de identificación):")
    correo = input("Ingrese el correo electrónico: ")
    direccion = input("Ingrese la dirección de residencia: ")
     
    return pri_nombre, seg_nombre, pri_apellido, seg_apellido, documento, correo, direccion

def mostrar_clientes(clientes):
    if clientes:
        print("\n--- Lista de Clientes ---")
        for cliente in clientes:
            print(cliente)
    else:
        print("No hay clientes registrados.")

def obtener_id_cliente():
    return input("Ingrese el ID del cliente: ")

def mostrar_mensaje(mensaje):
    print(mensaje)
