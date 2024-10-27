# ARGBroker Demo

## Descripción

**ARGBroker Demo** es una aplicación de simulación de un broker de bolsa, diseñada para el mercado financiero de Buenos Aires (MERVAL). Este proyecto permite a los inversores simular transacciones de compra y venta de acciones en tiempo real, así como gestionar sus portafolios personales.


## Requerimientos

- **Python 3.8+**
- **MySQL**
- Biblioteca de Python:
  - `mysql-connector-python` 
  (para instalarla: `pip install mysql-connector-python`)

## Configuración Inicial

1. **Configurar la base de datos MySQL**: 
   Crear la base de datos y tabla `inversores` ejecutando el siguiente script en MySQL:

   ```sql
   CREATE DATABASE broker_ispc;
   
   USE broker_ispc;
   
   CREATE TABLE inversores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    cuil VARCHAR(11) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    contraseña VARCHAR(255) NOT NULL,
    saldo DECIMAL(10, 2) DEFAULT 0,
    total_invertido DECIMAL(10, 2) DEFAULT 0,
    rendimiento_total DECIMAL(10, 2) DEFAULT 0,
    intentos_fallidos INT DEFAULT 0,
    bloqueado BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

2. **Configurar la conexión a MySQL**:
    En `db.py`, modificar los datos de conexión:

    ```
    import mysql.connector

    def conectar_db():
        return mysql.connector.connect(
            host="localhost",
            user="<tu usuario>",
            password="<tu password>",
            database="broker_ispc"
        )

## Uso
Para ejecutar el programa, abre la terminal y ejecuta:

 `python src/main.py`

Al ejecutar el programa, se te presentará un menú de opciones:

    1. Iniciar sesión
    2. Registrar nuevo usuario
    3. Ver lista de inversores
    4. Salir
    Selecciona una opción:

## Convenciones de Nomenclatura

Este proyecto sigue las convenciones de PEP 8:

    -Nombres de archivos y funciones: Formato snake_case, ej., main.py, mostrar_datos_cuenta. 
    -Clases: Formato PascalCase, ej., Inversor.
    -Constantes: Letras mayúsculas en snake_case, ej., MAX_INTENTOS.


## Authors

- [@santyagote](https://github.com/santyagote)
- [@ccauci](https://github.com/ccauci)
- [@SrLachy](https://github.com/SrLachy)
