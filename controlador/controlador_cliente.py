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
    
    # Verificar si el cliente existe antes de continuar
    if not cliente.cliente_existe(id_cliente):
        vista_cliente.mostrar_mensaje("❌ No existe un cliente con ese ID en la base de datos.")
        return
        
    datos_cliente = vista_cliente.obtener_datos_cliente()
    pri_nombre, seg_nombre, pri_apellido, seg_apellido, documento, correo, direccion = datos_cliente

    if correo and not validar_correo(correo):
        vista_cliente.mostrar_mensaje("❌ Error: Formato de correo electrónico inválido")
        return

    success, mensaje = cliente.actualizar_cliente(id_cliente, pri_nombre, seg_nombre, pri_apellido, seg_apellido, correo, direccion, documento)
    if success:
        vista_cliente.mostrar_mensaje(f"✅ {mensaje}")
    else:
        vista_cliente.mostrar_mensaje(f"❌ {mensaje}")