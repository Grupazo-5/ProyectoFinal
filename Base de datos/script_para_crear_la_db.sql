CREATE DATABASE IF NOT EXISTS broker_ispc;
USE broker_ispc;
CREATE TABLE inversores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    cuil VARCHAR(11) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    contraseña VARCHAR(255) NOT NULL,
    saldo FLOAT DEFAULT 0,
    total_invertido FLOAT DEFAULT 0,
    rendimiento_total FLOAT DEFAULT 0,
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
    precio_compra FLOAT NOT NULL,
    precio_venta FLOAT NOT NULL,
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
    precio_transaccion FLOAT  NOT NULL,
    comision FLOAT  NOT NULL,
    total FLOAT NOT NULL,
    FOREIGN KEY (inversor_id) REFERENCES inversores(id),
    FOREIGN KEY (activo_id) REFERENCES activos(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);