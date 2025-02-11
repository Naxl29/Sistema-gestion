import modelo
import modelo.cliente
import vista
import vista.vista_cliente

def crear_cliente():
    datos_cliente = vista.vista_cliente.obtener_datos_cliente()
    pri_nombre, seg_nombre, pri_apellido, seg_apellido, documento, correo, direccion = datos_cliente

    if modelo.cliente.insertar_cliente(pri_nombre, seg_nombre, pri_apellido, seg_apellido, documento, correo, direccion):
        vista.vista_cliente.mostrar_mensaje("Cliente agregado exitosamente.")
    else:
        vista.vista_cliente.mostrar_mensaje("Error al agregar el cliente.")

def mostrar_clientes():
    clientes = modelo.cliente.obtener_clientes()
    vista.vista_cliente.mostrar_clientes(clientes)

def eliminar_cliente():
    id_cliente = vista.vista_cliente.obtener_id_cliente()
    if modelo.cliente.eliminar_cliente(id_cliente):
        vista.vista_cliente.mostrar_mensaje("Cliente eliminado exitosamente.")
    else:
        vista.vista_cliente.mostrar_mensaje("No se encontró un cliente con ese ID.")

def actualizar_cliente():
    id_cliente = vista.vista_cliente.obtener_id_cliente()
    datos_cliente = vista.vista_cliente.obtener_datos_cliente()
    pri_nombre, seg_nombre, pri_apellido, seg_apellido, documento, correo, direccion = datos_cliente

    if modelo.cliente.actualizar_cliente(id_cliente, pri_nombre, seg_nombre, pri_apellido, seg_apellido, correo, direccion, documento):
        vista.vista_cliente.mostrar_mensaje("Cliente actualizado exitosamente.")
    else:
        vista.vista_cliente.mostrar_mensaje("Error al actualizar el cliente.")

def mostrar_menu_cliente():
    while True:
        vista.vista_cliente.mostrar_menu()
        opcion = input("Ingrese la opción que desea: ")

        if opcion == "1":
            crear_cliente()
        elif opcion == "2":
            mostrar_clientes()
        elif opcion == "3":
            eliminar_cliente()
        elif opcion == "4":
            actualizar_cliente()
        elif opcion == "5":
            vista.vista_cliente.mostrar_mensaje("Saliendo del programa...")
            break
        else:
            vista.vista_cliente.mostrar_mensaje("El valor ingresado no es válido, intente de nuevo.")
