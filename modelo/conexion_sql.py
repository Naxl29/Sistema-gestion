import mysql.connector
from mysql.connector import Error

# Función para conectar con MySQL
def conexion():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ventas_2025"
        )
        if conn.is_connected():
            print("Conexión exitosa a la base de datos")
            return conn
    except Error as e:
        print(f"Error en la conexión: {e}")
        return None
