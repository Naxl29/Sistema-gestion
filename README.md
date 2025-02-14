# Sistema de Gestión de Clientes

Este es un sistema de gestión de clientes desarrollado en Python que permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre una base de datos de clientes. El sistema está diseñado con una arquitectura MVC (Modelo-Vista-Controlador) para mantener un código organizado y mantenible.

## Características

- ✨ Crear nuevos clientes con validación de datos
- 📋 Listar todos los clientes registrados
- 🔄 Actualizar información de clientes existentes
- ❌ Eliminar clientes del sistema
- 🔍 Validación de correos electrónicos
- 🛡️ Validación de datos de entrada
- 📝 Manejo de errores y mensajes informativos

## Tecnologías Utilizadas

- **Python 3.x**: Lenguaje de programación principal
- **MySQL**: Sistema de gestión de base de datos
- **MySQL Connector/Python**: Biblioteca para la conexión con MySQL

## Estructura del Proyecto

```
proyecto/
├── controllers/
│   └── controlador_cliente.py
├── models/
│   └── cliente.py
├── views/
│   └── vista_cliente.py
├── main.py
└── README.md
```

## Arquitectura

El proyecto sigue el patrón de arquitectura MVC:

- **Modelo (models/)**: Maneja la lógica de negocio y la interacción con la base de datos
- **Vista (views/)**: Gestiona la interfaz de usuario y la presentación de datos
- **Controlador (controllers/)**: Coordina las acciones entre el modelo y la vista

## Librerías Utilizadas

- **mysql-connector-python**: Proporciona la conexión y operaciones con la base de datos MySQL
- **re**: Módulo de Python para el manejo de expresiones regulares (validación de correos)

## Base de Datos

El sistema utiliza una base de datos MySQL llamada `ventas_2025` con las siguientes tablas:

- **personas**: Almacena la información personal de los clientes
- **clientes**: Tabla relacionada que identifica qué personas son clientes

## Requisitos del Sistema

1. Python 3.x instalado
2. MySQL Server instalado y configurado
3. Librería mysql-connector-python instalada

## Instalación

1. Clonar el repositorio
2. Instalar las dependencias:
   ```bash
   pip install mysql-connector-python
   ```
3. Configurar la conexión a la base de datos en `config.py`
4. Ejecutar el script principal:
   ```bash
   python main.py
   ```

## Características de Validación

- Validación de nombres y apellidos (solo letras permitidas)
- Validación de documento de identidad (solo números)
- Validación de formato de correo electrónico
- Verificación de existencia de cliente antes de actualizar o eliminar
- Manejo de campos obligatorios y opcionales

## Manejo de Errores

El sistema incluye un robusto manejo de errores para:
- Errores de conexión a la base de datos
- Validación de datos de entrada
- Operaciones CRUD fallidas
- Intentos de actualizar o eliminar registros inexistentes

## Mejores Prácticas Implementadas

- Separación de responsabilidades (MVC)
- Validación de datos de entrada
- Manejo de excepciones
- Código modular y reutilizable
- Mensajes de usuario informativos
- Cierre adecuado de conexiones a la base de datos
