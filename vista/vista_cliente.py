def mostrar_menu():
    print("=== Menú Cliente ===")
    print("1. Crear Cliente")
    print("2. Mostrar Clientes")
    print("3. Eliminar Cliente")
    print("4. Actualizar Cliente")
    print("5. Salir")

def obtener_datos_cliente():
    while True:
        pri_nombre = input("Ingrese el primer nombre (obligatorio): ").strip()
        if pri_nombre and pri_nombre.replace(" ", "").isalpha():
            break
        print("❌ El primer nombre es obligatorio y solo debe contener letras.")
    
    while True:
        seg_nombre = input("Ingrese el segundo nombre (opcional): ").strip()
        if not seg_nombre:  # Si está vacío, es válido porque es opcional
            seg_nombre = ""
            break
        if seg_nombre.replace(" ", "").isalpha():
            break
        print("❌ El segundo nombre solo debe contener letras.")

    while True:
        pri_apellido = input("Ingrese el primer apellido (obligatorio): ").strip()
        if pri_apellido and pri_apellido.replace(" ", "").isalpha():
            break
        print("❌ El primer apellido es obligatorio y solo debe contener letras.")
    
    while True:
        seg_apellido = input("Ingrese el segundo apellido (opcional): ").strip()
        if not seg_apellido:  # Si está vacío, es válido porque es opcional
            seg_apellido = ""
            break
        if seg_apellido.replace(" ", "").isalpha():
            break
        print("❌ El segundo apellido solo debe contener letras.")
    
    while True:
        documento = input("Ingrese el documento (obligatorio): ").strip()
        if documento and documento.isdigit():
            break
        print("❌ El documento debe contener solo números.")
    
    correo = input("Ingrese el correo electrónico (opcional): ").strip()
    direccion = input("Ingrese la dirección de residencia (opcional): ").strip()
     
    return pri_nombre, seg_nombre, pri_apellido, seg_apellido, documento, correo, direccion

def mostrar_clientes(clientes):
    if not clientes:
        print("No hay clientes registrados.")
        return

    print("=== Lista de Clientes ===")
    for cliente in clientes:
        print("-------------------")
        print(f"ID: {cliente['id_cliente']}")
        print(f"Nombre: {cliente['pri_nombre']} {cliente['seg_nombre'] or ''}")
        print(f"Apellidos: {cliente['pri_apellido']} {cliente['seg_apellido'] or ''}")
        print(f"Correo: {cliente['correo_electronico'] or 'No especificado'}")
        print(f"Dirección: {cliente['direccion_residencia'] or 'No especificada'}")

def obtener_id_cliente():
    while True:
        id_cliente = input("Ingrese el ID del cliente: ").strip()
        if id_cliente and id_cliente.isdigit():
            return id_cliente
        print("El ID debe ser un número válido.")

def mostrar_mensaje(mensaje):
    print(f"{mensaje}")

def ejecutar_menu():
    from controlador import controlador_cliente
    
    while True:
        mostrar_menu()
        opcion = input("Ingrese la opción que desea: ")

        if opcion == "1":
            controlador_cliente.crear_cliente()
        elif opcion == "2":
            controlador_cliente.mostrar_clientes()
        elif opcion == "3":
            controlador_cliente.eliminar_cliente()
        elif opcion == "4":
            controlador_cliente.actualizar_cliente()
        elif opcion == "5":
            mostrar_mensaje("👋 ¡Hasta luego!")
            break
        else:
            mostrar_mensaje("❌ Opción inválida. Por favor, intente de nuevo.")