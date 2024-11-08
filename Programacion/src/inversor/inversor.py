from src.portafolio.portafolio import Portafolio
from src.usuarios.usuarios import Usuario

class Inversor:
    
    def __init__(self, id_inversor):
        self.id_inversor = id_inversor
        self.nombre, self.apellido, self.cuil, self.email = Usuario.obtener_inversor(id_inversor)
        self.portafolio = Portafolio(id_inversor)
        
    def modificar_mail(nuevo_email):
        Usuario.modificar_usuario("inversores","email",nuevo_email)
    def modificar_contraseña(contraseña_actual, nueva_contraseña):
        if contraseña_actual:
            Usuario.modificar_usuario("inversores", "contraseña", nueva_contraseña)
    def mostrar_datos_cuenta (self):
        print(f"\nDatos de la cuenta de {self.nombre} {self.apellido}:")
        print(f"Saldo: {self.portafolio.saldo}")
        print(f"Total invertido: {self.portafolio.total_invertido}")
        print(f"Rendimiento total: {self.portafolio.rendimiento_total}")
    
    @staticmethod
    def registrar_nuevo_inversor (nombre, apellido, cuil, email, contrasena):
        Usuario.crear_usuario(nombre, apellido, cuil, email, contrasena)
        
    