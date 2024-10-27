from db import conectar_db

class Inversor:
    
    @staticmethod
    def registrar_usuario(nombre, apellido, cuil, email, contrasena, saldo=100000):
        conexion = conectar_db()
        cursor = conexion.cursor()
        
        try:
            cursor.execute("""
                INSERT INTO inversores (nombre, apellido, cuil, email, contraseña, saldo)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (nombre, apellido, cuil, email, contrasena, saldo))
            
            conexion.commit()
            print(f"Usuario {nombre} {apellido} registrado con éxito.")
        except Exception as e:
            print(f"Error al registrar usuario: {e}")
        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    def login(email, contrasena):
        conexion = conectar_db()
        cursor = conexion.cursor()
        
        # Modificamos la consulta para asegurarnos del orden correcto de los campos
        cursor.execute("""
            SELECT 
                id, 
                nombre, 
                apellido, 
                saldo, 
                total_invertido, 
                rendimiento_total,
                contraseña
            FROM inversores 
            WHERE email = %s
        """, (email,))
        
        usuario = cursor.fetchone()
        
        cursor.close()
        conexion.close()
        
        if usuario and usuario[6] == contrasena:  # Verificamos la contraseña (índice 6)
            inversor = Inversor()
            # Asignamos los valores en el orden correcto
            inversor.id = usuario[0]
            inversor.nombre = usuario[1]
            inversor.apellido = usuario[2]
            inversor.saldo = usuario[3]         # Saldo es el cuarto campo
            inversor.total_invertido = usuario[4]
            inversor.rendimiento_total = usuario[5]
            return inversor
        else:
            print("Credenciales incorrectas.")
            return None
    
    @staticmethod
    def listar_inversores():
        conexion = conectar_db()
        cursor = conexion.cursor()
        
        cursor.execute("SELECT nombre, apellido, email FROM inversores")
        inversores = cursor.fetchall()
        
        if inversores:
            for inversor in inversores:
                nombre, apellido, email = inversor
                print(f"Nombre: {nombre}, Apellido: {apellido}, Email: {email}")
        else:
            print("No hay inversores registrados.")
        
        cursor.close()
        conexion.close()

    def mostrar_datos_cuenta(self):
        print(f"\nDatos de la cuenta de {self.nombre} {self.apellido}:")
        print(f"Saldo: ${self.saldo:,.2f}")  # Formateo para mostrar el saldo como moneda
        print(f"Total invertido: ${self.total_invertido:,.2f}" if self.total_invertido else "Total invertido: $0.00")
        print(f"Rendimiento total: ${self.rendimiento_total:,.2f}" if self.rendimiento_total else "Rendimiento total: $0.00")

    def listar_portafolio(self):
        conexion = conectar_db()
        cursor = conexion.cursor()
        
        cursor.execute("""
            SELECT activos.nombre_activo, portafolio.cantidad_acciones, activos.precio_compra, activos.precio_venta
            FROM portafolio
            JOIN activos ON portafolio.activo_id = activos.id
            WHERE portafolio.inversor_id = %s
        """, (self.id,))
        
        activos_en_portafolio = cursor.fetchall()
        
        if activos_en_portafolio:
            for activo in activos_en_portafolio:
                nombre_activo, cantidad_acciones, precio_compra, precio_venta = activo
                rendimiento = precio_venta - precio_compra
                print(f"Activo: {nombre_activo}, Cantidad: {cantidad_acciones}, Precio de compra: ${precio_compra:,.2f}, Precio de venta: ${precio_venta:,.2f}, Rendimiento: ${rendimiento:,.2f}")
        else:
            print("No tienes activos en tu portafolio.")
        
        cursor.close()
        conexion.close()