from src.usuarios.usuarios import Usuario
from conectar_db import conectar_db
    
def registrar_transaccion (id_inversor,id_activo, cantidad, tipo_de_transaccion):
    conexion = conectar_db()
    cursor = conexion.cursor()
    precio = Usuario.obtener_precio_de_activo(id_activo)[f"{tipo_de_transaccion}"]
    total_transaccion= precio * cantidad
    comision=total_transaccion*.01
    cursor.execute("""
                INSERT INTO transacciones (inversor_id, activo_id, tipo_transaccion, cantidad_acciones, precio_transaccion, comision, total)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (id_inversor, id_activo, tipo_de_transaccion, cantidad, precio, comision, total_transaccion))
            
    conexion.commit()
    cursor.close()
    conexion.close()
    
def realizar_compra(inversor_id,activo_id,cantidad,saldo):

    conexion = conectar_db()
    cursor = conexion.cursor()
    precio_compra= Usuario.obtener_precio_de_activo(activo_id)["compra"]
    total_compra= precio_compra*cantidad*1.01
    cursor.execute("UPDATE inversores SET saldo = %s WHERE id = %s", (saldo, inversor_id))
    cursor.execute("UPDATE inversores SET total_invertido = %s WHERE id = %s", (total_compra, inversor_id))       
    conexion.commit()
    cursor.close()
    conexion.close()
    registrar_transaccion(inversor_id, activo_id, cantidad, "compra")

def realizar_venta(inversor_id,activo_id,cantidad,saldo):
    conexion = conectar_db()
    cursor = conexion.cursor()
    precio_compra= Usuario.obtener_precio_de_activo(activo_id)["venta"]
    total_compra= precio_compra*cantidad*1.01
    cursor.execute("UPDATE inversores SET saldo = %s WHERE id = %s", (saldo, inversor_id))
    cursor.execute("UPDATE inversores SET total_invertido = %s WHERE id = %s", (total_compra, inversor_id))  
    conexion.commit()
    cursor.close()
    conexion.close()
    registrar_transaccion(inversor_id,activo_id, cantidad,"venta")
    
def actualizar_saldo(saldo_actual):
    Usuario.modificar_usuario("inversores","saldo", saldo_actual)