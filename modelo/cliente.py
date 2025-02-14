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

def cliente_existe(id_cliente):
    conn = conexion()
    if conn is None:
        return False

    try:
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT COUNT(*) as count FROM personas WHERE id_cliente = %s"
        cursor.execute(sql, (id_cliente,))
        resultado = cursor.fetchone()
        return resultado['count'] > 0
    except Exception as e:
        print(f"Error al verificar el cliente: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

def insertar_cliente(pri_nombre, seg_nombre, pri_apellido, seg_apellido, documento, correo, direccion):
    if not pri_nombre or not pri_apellido or not documento:
        print("Los campos primer nombre, primer apellido y documento son obligatorios")
        return False

    conn = conexion()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()
        
        # Primero insertamos en la tabla personas
        sql = """INSERT INTO personas (pri_nombre, seg_nombre, pri_apellido, seg_apellido, 
                 id_cliente, correo_electronico, direccion_residencia, fecha_registro)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, NOW())"""
        valores = (pri_nombre, seg_nombre, pri_apellido, seg_apellido, documento, correo, direccion)
        cursor.execute(sql, valores)
        
        # Luego insertamos en la tabla clientes
        sql_cliente = "INSERT INTO clientes (id_cliente) VALUES (%s)"
        cursor.execute(sql_cliente, (documento,))
        
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
        cursor = conn.cursor(dictionary=True)
        # Modificamos la consulta para obtener solo de la tabla personas
        cursor.execute("""
            SELECT * FROM personas 
            ORDER BY fecha_registro DESC
        """)
        clientes = cursor.fetchall()
        if clientes:
            print(f"\nSe encontraron {len(clientes)} registros en la base de datos")
        return clientes
    except Exception as e:
        print(f"Error al obtener los clientes: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

def eliminar_cliente(id_cliente):
    if not cliente_existe(id_cliente):
        return False

    conn = conexion()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()
        # Primero eliminamos de la tabla clientes
        sql_cliente = "DELETE FROM clientes WHERE id_cliente = %s"
        cursor.execute(sql_cliente, (id_cliente,))
        
        # Luego eliminamos de la tabla personas
        sql_persona = "DELETE FROM personas WHERE id_cliente = %s"
        cursor.execute(sql_persona, (id_cliente,))
        
        conn.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Error al eliminar el cliente: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

def actualizar_cliente(id_cliente, pri_nombre, seg_nombre, pri_apellido, seg_apellido, correo, direccion, documento):
    if not cliente_existe(id_cliente):
        return False, "Cliente no encontrado"

    if not pri_nombre or not pri_apellido or not documento:
        return False, "Los campos primer nombre, primer apellido y documento son obligatorios"

    conn = conexion()
    if conn is None:
        return False, "Error de conexión a la base de datos"

    try:
        cursor = conn.cursor()
        sql = """UPDATE personas 
                 SET pri_nombre = %s, seg_nombre = %s, pri_apellido = %s, 
                     seg_apellido = %s, correo_electronico = %s, 
                     direccion_residencia = %s
                 WHERE id_cliente = %s"""
        valores = (pri_nombre, seg_nombre, pri_apellido, seg_apellido, 
                  correo, direccion, id_cliente)
        cursor.execute(sql, valores)
        conn.commit()
        return True, "Cliente actualizado exitosamente"
    except Exception as e:
        return False, f"Error al actualizar el cliente: {e}"
    finally:
        cursor.close()
        conn.close()