from modelo import cliente
from vista import vista_cliente
import re

def validar_correo(correo):
    if not correo:
        return True
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(patron, correo))

def crear_cliente():
    datos_cliente = vista_cliente.obtener_datos_cliente()
    pri_nombre, seg_nombre, pri_apellido, seg_apellido, documento, correo, direccion = datos_cliente

    if correo and not validar_correo(correo):
        vista_cliente.mostrar_mensaje("Error: Formato de correo electrónico inválido")
        return

    if cliente.insertar_cliente(pri_nombre, seg_nombre, pri_apellido, seg_apellido, documento, correo, direccion):
        vista_cliente.mostrar_mensaje("✅ Cliente agregado exitosamente.")
    else:
        vista_cliente.mostrar_mensaje("❌ Error al agregar el cliente.")

def mostrar_clientes():
    clientes = cliente.obtener_clientes()
    vista_cliente.mostrar_clientes(clientes)

def eliminar_cliente():
    id_cliente = vista_cliente.obtener_id_cliente()
    if cliente.eliminar_cliente(id_cliente):
        vista_cliente.mostrar_mensaje("✅ Cliente eliminado exitosamente.")
    else:
        vista_cliente.mostrar_mensaje("❌ No se encontró un cliente con ese ID.")

def actualizar_cliente():
    id_cliente = vista_cliente.obtener_id_cliente()
    datos_cliente = vista_cliente.obtener_datos_cliente()
    pri_nombre, seg_nombre, pri_apellido, seg_apellido, documento, correo, direccion = datos_cliente

    if correo and not validar_correo(correo):
        vista_cliente.mostrar_mensaje("Error: Formato de correo electrónico inválido")
        return

    if cliente.actualizar_cliente(id_cliente, pri_nombre, seg_nombre, pri_apellido, seg_apellido, correo, direccion, documento):
        vista_cliente.mostrar_mensaje("✅ Cliente actualizado exitosamente.")
    else:
        vista_cliente.mostrar_mensaje("❌ Error al actualizar el cliente.")