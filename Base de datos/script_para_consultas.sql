USE broker_ispc;

-- Sentencias DML de tipo INSERT

INSERT INTO inversores (nombre, apellido, cuil, email, contraseña, saldo, total_invertido, rendimiento_total)
VALUES 
('Juan', 'Pérez', '20304050607', 'juan.perez@email.com', '123456', 10000, 0, 0),
('Ana', 'López', '27304050608', 'ana.lopez@email.com', '123456', 5000, 0, 0),
('Carlos', 'García', '23304050609', 'carlos.garcia@email.com', '123456', 8000, 0, 0),
('María', 'Rodríguez', '25304050610', 'maria.rodriguez@email.com', '123456', 12000, 0, 0),
('Lucía', 'Fernández', '26304050611', 'lucia.fernandez@email.com', '123456', 15000, 0, 0);

INSERT INTO activos (nombre_activo, precio_compra, precio_venta)
VALUES 
('Empresa A', 100, 110),
('Empresa B', 200, 210),
('Empresa C', 300, 310),
('Empresa D', 400, 420),
('Empresa E', 500, 530);

-- Consultas de tipo UPDATE

UPDATE inversores 
SET email = 'juan.perez99@email.com'
WHERE id = 10;

UPDATE portafolio
SET cantidad_acciones = 100
WHERE inversor_id = 10 AND activo_id = 2;

UPDATE inversores
SET contraseña = '654321'
WHERE email = 'maria.rodriguez@email.com';

UPDATE activos
SET precio_venta = 550
WHERE nombre_activo = 'Empresa A';

UPDATE inversores 
SET saldo = saldo + 5000,
    rendimiento_total = rendimiento_total + 500
WHERE cuil = '20304050607';

-- Consultas de tipo SELECT

SELECT * FROM inversores;

SELECT * FROM activos;

SELECT nombre, apellido, saldo FROM inversores WHERE cuil = '20304050607';

SELECT * FROM transacciones WHERE inversor_id = 10;

SELECT nombre, apellido, rendimiento_total FROM inversores;


-- Consulta Multitabla N° 1: Sirve para obtener el saldo y rendimiento total de cada inversor junto con sus activos en el portafolio

SELECT inversores.nombre, inversores.apellido, inversores.saldo, inversores.rendimiento_total,
       activos.nombre_activo, portafolio.cantidad_acciones, portafolio.precio_compra
FROM inversores
LEFT JOIN portafolio ON inversores.id = portafolio.inversor_id
LEFT JOIN activos ON portafolio.activo_id = activos.id;

-- Consulta Multitabla N°2: Sirve para ver todas las transacciones de compra y venta realizadas por cada inversor, incluyendo detalles del activo y la comisión aplicada

SELECT inversores.nombre, inversores.apellido, activos.nombre_activo, transacciones.tipo_transaccion,
       transacciones.cantidad_acciones, transacciones.precio_transaccion, transacciones.comision, transacciones.total
FROM transacciones
INNER JOIN inversores ON transacciones.inversor_id = inversores.id
INNER JOIN activos ON transacciones.activo_id = activos.id
ORDER BY transacciones.created_at DESC;

-- Consulta Multitabla N°3: Sirve para obtener el valor total invertido por cada inversor en su portafolio actual

SELECT inversores.nombre, inversores.apellido,
       SUM(portafolio.cantidad_acciones * portafolio.precio_compra) AS total_invertido
FROM inversores
INNER JOIN portafolio ON inversores.id = portafolio.inversor_id
GROUP BY inversores.id;