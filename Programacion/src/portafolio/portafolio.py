from src.usuarios.usuarios import Usuario
from src.transacciones.transacciones import realizar_compra,realizar_venta, actualizar_saldo

class Portafolio:
    
    def __init__(self, id):
        if Usuario.listar_portafolio(id):
            self.actualizar_portafolio(id)
            self.id_usuario=id
        else:
            self.acciones = {}
            self.saldo = 1000000
            self.total_invertido=0
            self.rendimiento_total=0
            self.id_usuario=id
            actualizar_saldo(float(1000000))
        

    def comprar(self, activo_id, cantidad):
        activo = Usuario.obtener_precio_de_activo(activo_id)
    
        if activo:
            precio_compra = activo["compra"]
            nombre_activo = activo["nombre"]
            total_compra = precio_compra * cantidad
            comision = total_compra * float(0.01)
            total_con_comision = total_compra + comision
            if self.saldo >= total_con_comision:
                saldo_actual= self.saldo - total_con_comision
                realizar_compra(self.id_usuario, activo_id, cantidad, saldo_actual)
                self.actualizar_portafolio(self.id_usuario)
                print(f"Has comprado {cantidad} acciones de {nombre_activo} por un total de {total_con_comision} (comisión incluida).")
            else: print("No tienes saldo suficiente para realizar la compra.")
        else:
            print("Activo no encontrado.")
    
    def vender(self, activo_id, cantidad):
        
        if self.acciones[activo_id][1]:
            cantidad_en_portafolio = self.acciones[activo_id][1]
        
            if cantidad <= cantidad_en_portafolio:
                activo = Usuario.obtener_precio_de_activo(activo_id)
                if activo:
                    precio_venta = activo["venta"]
                    nombre_activo = activo["nombre"]
                    total_venta = precio_venta * cantidad
                    comision = total_venta * 0.01
                    total_con_comision = total_venta - comision
                    saldo_actual= self.saldo + total_con_comision
                    realizar_venta(self.id_usuario,activo_id, cantidad,saldo_actual)
                    self.actualizar_portafolio(self.id_usuario)
                    print(f"Has vendido {cantidad} acciones de {nombre_activo} por un total de {total_con_comision} (comisión incluida).")
                else: print("No tienes saldo suficiente para realizar la compra.")
        else:
            print("No tienes suficientes acciones para vender.")
    def listar_portafolio(self):
        diccionario = Usuario.obtener_nombres_de_activos()
        for id, accion in self.acciones.items():
            print(f"Id:{id}, Activo: {diccionario[id]}, Cantidad: {accion[0]}, Valor: {accion[1]} ")
    
    def actualizar_portafolio(self, id_usuario):
        self.acciones,self.saldo, self.total_invertido,self.rendimiento_total=Usuario.listar_portafolio(id_usuario)
    @staticmethod
    def listar_acciones():
        acciones = Usuario.obtener_nombres_de_activos ()
        for id in acciones:
            accion= Usuario.obtener_precio_de_activo(id)
            print(f"ID: {id}, Nombre: {accion["nombre"]}, Precio de compra: {accion["compra"]}, Precio de venta: {accion["venta"]}")