import mysql.connector
from mysql.connector import Error

def conexion():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ventas_2025"
        )
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Error en la conexión: {e}")
        return None

def insertar_cliente(pri_nombre, seg_nombre, pri_apellido, seg_apellido, documento, correo, direccion):
    conn = conexion()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()
        sql = """INSERT INTO personas (pri_nombre, seg_nombre, pri_apellido, seg_apellido, documento, correo_electronico, direccion_residencia, fecha_registro)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, NOW())"""
        valores = (pri_nombre, seg_nombre, pri_apellido, seg_apellido, documento, correo, direccion)
        cursor.execute(sql, valores)
        conn.commit()
        return True
    except Exception as e:
        print(f"Error al agregar cliente: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

def obtener_clientes():
    conn = conexion()
    if conn is None:
        return []

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM personas")
        clientes = cursor.fetchall()
        return clientes
    except Exception as e:
        print(f"Error al obtener los clientes: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

def eliminar_cliente(id_cliente):
    conn = conexion()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()
        sql = "DELETE FROM personas WHERE id_cliente = %s"
        cursor.execute(sql, (id_cliente,))
        conn.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Error al eliminar el cliente: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

def actualizar_cliente(id_cliente, pri_nombre, seg_nombre, pri_apellido, seg_apellido, correo, direccion, documento):
    conn = conexion()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()
        sql = """UPDATE personas SET pri_nombre = %s, seg_nombre = %s, pri_apellido = %s, seg_apellido = %s, correo_electronico = %s, direccion_residencia = %s, documento = %s
                 WHERE id_cliente = %s"""
        valores = (pri_nombre, seg_nombre, pri_apellido, seg_apellido, correo, direccion, documento, id_cliente)
        cursor.execute(sql, valores)
        conn.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Error al actualizar el cliente: {e}")
        return False
    finally:
        cursor.close()
        conn.close()
