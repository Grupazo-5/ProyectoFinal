from db import conectar_db

def realizar_compra(inversor):
    activo_id = input("Introduce el ID del activo que quieres comprar: ")
    cantidad = int(input("Introduce la cantidad de acciones que quieres comprar: "))

    conexion = conectar_db()
    cursor = conexion.cursor()
    
    cursor.execute("SELECT nombre_activo, precio_compra FROM activos WHERE id = %s", (activo_id,))
    activo = cursor.fetchone()
    
    if activo:
        nombre_activo, precio_compra = activo
        total_compra = float(precio_compra) * cantidad
        
        if inversor.saldo >= total_compra:
            comision = total_compra * 0.01
            total_con_comision = total_compra + comision
            
            nuevo_saldo = float(inversor.saldo) - total_con_comision
            cursor.execute("UPDATE inversores SET saldo = %s WHERE id = %s", (nuevo_saldo, inversor.id))
            cursor.execute("UPDATE inversores SET total_invertido = %s WHERE id = %s", (total_compra, inversor.id))
            
            cursor.execute("""
                INSERT INTO portafolio (inversor_id, activo_id, cantidad_acciones, precio_compra)
                VALUES (%s, %s, %s, %s)
            """, (inversor.id, activo_id, cantidad, precio_compra))
            
            cursor.execute("""
                INSERT INTO transacciones (inversor_id, activo_id, tipo_transaccion, cantidad_acciones, precio_transaccion, comision, total)
                VALUES (%s, %s, 'compra', %s, %s, %s, %s)
            """, (inversor.id, activo_id, cantidad, precio_compra, comision, total_con_comision))
            
            conexion.commit()
            print(f"Has comprado {cantidad} acciones de {nombre_activo} por un total de {total_con_comision} (comisión incluida).")
        else:
            print("No tienes saldo suficiente para realizar la compra.")
    else:
        print("Activo no encontrado.")
    
    cursor.close()
    conexion.close()

def realizar_venta(inversor):
    activo_id = input("Introduce el ID del activo que quieres vender: ")
    cantidad = int(input("Introduce la cantidad de acciones que quieres vender: "))

    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT cantidad_acciones, precio_compra
        FROM portafolio
        WHERE inversor_id = %s AND activo_id = %s
    """, (inversor.id, activo_id))
    
    portafolio_activo = cursor.fetchone()

    if portafolio_activo:
        cantidad_en_portafolio, precio_compra = portafolio_activo
        
        if cantidad <= cantidad_en_portafolio:
            cursor.execute("SELECT nombre_activo, precio_venta FROM activos WHERE id = %s", (activo_id,))
            activo = cursor.fetchone()
            
            if activo:
                nombre_activo, precio_venta = activo
                total_venta = float(precio_venta) * cantidad
                comision = total_venta * 0.01
                total_con_comision = total_venta - comision
                
                nuevo_saldo = float(inversor.saldo) + total_con_comision
                cursor.execute("UPDATE inversores SET saldo = %s WHERE id = %s", (nuevo_saldo, inversor.id))
                
                nueva_cantidad = cantidad_en_portafolio - cantidad
                if nueva_cantidad == 0:
                    cursor.execute("DELETE FROM portafolio WHERE inversor_id = %s AND activo_id = %s", (inversor.id, activo_id))
                else:
                    cursor.execute("UPDATE portafolio SET cantidad_acciones = %s WHERE inversor_id = %s AND activo_id = %s", (nueva_cantidad, inversor.id, activo_id))
                
                cursor.execute("""
                    INSERT INTO transacciones (inversor_id, activo_id, tipo_transaccion, cantidad_acciones, precio_transaccion, comision, total)
                    VALUES (%s, %s, 'venta', %s, %s, %s, %s)
                """, (inversor.id, activo_id, cantidad, precio_venta, comision, total_con_comision))
                
                conexion.commit()
                print(f"Has vendido {cantidad} acciones de {nombre_activo} por un total de {total_con_comision} (comisión incluida).")
            else:
                print("Activo no encontrado.")
        else:
            print("No tienes suficientes acciones para vender.")
    else:
        print("No tienes este activo en tu portafolio.")

    cursor.close()
    conexion.close()

@staticmethod
def listar_acciones():
    conexion = conectar_db()
    cursor = conexion.cursor()
    
    cursor.execute("SELECT id, nombre_activo, precio_compra, precio_venta FROM activos")
    acciones = cursor.fetchall()
    
    if acciones:
        for accion in acciones:
            id, nombre_activo, precio_compra, precio_venta = accion
            print(f"ID: {id}, Nombre: {nombre_activo}, Precio de compra: {precio_compra}, Precio de venta: {precio_venta}")
    else:
        print("No hay acciones disponibles.")
    
    cursor.close()
    conexion.close()

@staticmethod
def listar_portafolio(inversor):
    conexion = conectar_db()
    cursor = conexion.cursor()
    
    cursor.execute("""
        SELECT a.id, a.nombre_activo, p.cantidad_acciones, p.precio_compra, p.precio_compra * p.cantidad_acciones AS valor_invertido
        FROM portafolio p
        JOIN activos a ON p.activo_id = a.id
        WHERE p.inversor_id = %s
    """, (inversor.id,))
    
    portafolio = cursor.fetchall()
    
    if portafolio:
        print("Portafolio de acciones:")
        for accion in portafolio:
            id, nombre_activo, cantidad_acciones, precio_compra, valor_invertido = accion
            print(f"ID: {id} Nombre: {nombre_activo}, Cantidad: {cantidad_acciones}, Precio de compra: {precio_compra}, Valor invertido: {valor_invertido}")
    else:
        print("No tienes acciones para vender")