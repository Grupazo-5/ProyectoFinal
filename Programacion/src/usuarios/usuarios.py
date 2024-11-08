from conectar_db import conectar_db

class Usuario:
    
    @staticmethod
    
    def crear_usuario(nombre, apellido, cuil, email, contrasena):
        conexion = conectar_db()
        cursor = conexion.cursor()
        
        try:
            cursor.execute("""
                INSERT INTO inversores (nombre, apellido, cuil, email, contraseña)
                VALUES (%s, %s, %s, %s, %s)
            """, (nombre, apellido, cuil, email, contrasena))
            
            conexion.commit()
            print(f"Usuario {nombre} {apellido} registrado con éxito.")
        except Exception as e:
            print(f"Error al registrar usuario: {e}")
        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    
    def es_usuario_valido(email, contrasena):
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("SELECT contraseña, id FROM inversores WHERE email = %s", (email,))
        usuario = cursor.fetchone()
        cursor.close()
        conexion.close() 
        if usuario:
            if usuario[0] == contrasena:
                return usuario[1]
        else:
            print("Credenciales incorrectas.")
            return False
         
    
    @staticmethod
    
    def obtener_inversor(id):
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre, apellido, cuil, email FROM inversores WHERE id = %s", (id,))
        inversor = cursor.fetchone()
        cursor.close()
        conexion.close() 
        return inversor
    
    @staticmethod
    
    def modificar_usuario(tabla, columna, nuevo_valor, id_a_modificar):
        conexion= conectar_db()
        cursor=conexion.cursor()
        query=f"UPDATE {tabla} SET {columna} = {nuevo_valor} WHERE id ={id_a_modificar};"
        cursor.execute(query)
        conexion.commit()
        cursor.close()
        conexion.close()
    
    @staticmethod
    
    def eliminar_usuario(id):
        conexion= conectar_db()
        cursor=conexion.cursor()
        query="DELETE * FROM inversor WHERE id = %s;"
        cursor.execute(query,(id,))
        conexion.commit()
        cursor.close()
        conexion.close()
    
    @staticmethod
    
    def listar_portafolio(id):
        conexion = conectar_db()
        cursor = conexion.cursor()
        
        cursor.execute("""
            SELECT activo_id, tipo_transaccion, cantidad_acciones, total
            FROM transacciones
            WHERE inversor_id = %s
        """, (id,))
        
        activos_en_portafolio = cursor.fetchall()
        cursor.execute("SELECT saldo, total_invertido FROM inversores WHERE id = %s", (id,))
        usuario = cursor.fetchone()
        saldo, total_invertido= usuario
        cursor.close()
        conexion.close()
        activos ={}
        rendimiento_total=0
        if activos_en_portafolio:
           
            for activo in activos_en_portafolio:
                id_activo, tipo_transaccion, cantidad_acciones, precio_total= activo
                try :
                    activos[id_activo]
                    if tipo_transaccion=="compra":
                        cantidad_acciones+=activos[id_activo][0]
                        rendimiento_total-=precio_total

                    else:
                        cantidad_acciones-=activos[id_activo][0]
                        rendimiento_total+=precio_total
                except:
                    
                    if tipo_transaccion=="compra" and not activos:
                        rendimiento_total-=precio_total
                    if tipo_transaccion=="venta" and not activos: 
                        rendimiento_total+=precio_total

                activos[id_activo]=(cantidad_acciones,precio_total)
                
        
        return (activos,saldo,total_invertido,rendimiento_total)
    
    @staticmethod
    
    def obtener_precio_de_activo (id_activo):
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre_activo, precio_compra, precio_venta FROM activos WHERE id = %s", (id_activo,))
        activo = cursor.fetchone()
        cursor.close()
        conexion.close()
        nombre_activo,precio_compra, precio_venta = activo
        return {"nombre":nombre_activo,"compra":precio_compra, "venta":precio_venta}
    @staticmethod
    
    def obtener_nombres_de_activos ():
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre_activo FROM activos")
        activos = cursor.fetchall()
        return {id_: nombre for id_, nombre in activos}