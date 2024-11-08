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
   Crear la base de datos ejecutando el siguiente script en MySQL:

   ```sql
   CREATE DATABASE IF NOT EXISTS broker_ispc;  
   
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
    
    CREATE TABLE recuperacion_contraseña (
        id INT AUTO_INCREMENT PRIMARY KEY,
        inversor_id INT,
        token VARCHAR(255) NOT NULL,
        expiracion TIMESTAMP NOT NULL,
        FOREIGN KEY (inversor_id) REFERENCES inversores(id)
    );
    
    CREATE TABLE activos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre_activo VARCHAR(100) NOT NULL,
        precio_compra DECIMAL(10, 2) NOT NULL,
        precio_venta DECIMAL(10, 2) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    
    CREATE TABLE portafolio (
        id INT AUTO_INCREMENT PRIMARY KEY,
        inversor_id INT,
        activo_id INT,
        cantidad_acciones INT NOT NULL,
        precio_compra DECIMAL(10, 2) NOT NULL,
        FOREIGN KEY (inversor_id) REFERENCES inversores(id),
        FOREIGN KEY (activo_id) REFERENCES activos(id),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    
    CREATE TABLE transacciones (
        id INT AUTO_INCREMENT PRIMARY KEY,
        inversor_id INT,
        activo_id INT,
        tipo_transaccion ENUM('compra', 'venta') NOT NULL,
        cantidad_acciones INT NOT NULL,
        precio_transaccion DECIMAL(10, 2) NOT NULL,
        comision DECIMAL(10, 2) NOT NULL,
        total DECIMAL(10, 2) NOT NULL,
        FOREIGN KEY (inversor_id) REFERENCES inversores(id),
        FOREIGN KEY (activo_id) REFERENCES activos(id),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAM
    );

2. **Configurar la conexión a MySQL**:
    En **`db.py`**, modificar los datos de conexión:

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

Al ejecutar el programa, se te presentará un menú de opciones como este:

    1. Iniciar sesión
    2. Registrar nuevo usuario
    3. Ver lista de inversores
    4. Salir
    Selecciona una opción:

Podrá seleccionar la opción que desee escribiendo el N° de la opcion y dando a Enter.

## Convenciones de Nomenclatura

Este proyecto sigue las convenciones de PEP 8:

- Nombres de archivos y funciones: Formato snake_case. 
Ejemplo: main.py, mostrar_datos_cuenta. 
- Clases: Formato PascalCase. 
Ejemplo: Inversor.
- Constantes: Letras mayúsculas en snake_case. 
Ejemplo: MAX_INTENTOS.


## Authors

- [@santyagote](https://github.com/santyagote)
- [@ccauci](https://github.com/ccauci)
- [@SrLachy](https://github.com/SrLachy)

