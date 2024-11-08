from src.login import login
from src.inversor import Inversor
def mostrar_menu_principal():
    print("\nMenú Principal:")
    print("1. Iniciar sesión")
    print("2. Registrar nuevo usuario")
    print("3. Salir")
    opcion = input("Selecciona una opción: ")
    return opcion

def mostrar_menu_inversor():
    print("\nMenú del Inversor:")
    print("1. Mostrar datos de cuenta")
    print("2. Listar activos del portafolio")
    print("3. Comprar acciones")
    print("4. Vender acciones")
    print("5. Cerrar sesión")
    opcion = input("Selecciona una opción: ")
    return opcion

def iniciar():
    while True:
        opcion = mostrar_menu_principal()
        
        if opcion == "1":  # Iniciar sesión
            email = input("Introduce tu email: ")
            contrasena = input("Introduce tu contraseña: ")
            id_inversor = login(email, contrasena)
            
            if id_inversor:
                inversor= Inversor(id_inversor)
                print(f"\nBienvenido, {inversor.nombre}!")
                
                while True:
                    opcion_inversor = mostrar_menu_inversor()
                    
                    if opcion_inversor == "1":  # Datos de la cuenta
                        inversor.mostrar_datos_cuenta()
                    elif opcion_inversor == "2":  # Listar activos del portafolio
                        inversor.portafolio.listar_portafolio()
                    elif opcion_inversor == "3":  # Comprar acciones
                        print("\nLista de acciones disponibles:")
                        inversor.portafolio.listar_acciones()
                        id=int(input("Ingrese el numero de id de la accion que quiere comprar: "))
                        cantidad= int(input("Ingrese la cantidad de acciones que desea comprar: "))
                        inversor.portafolio.comprar(id, cantidad)
                    elif opcion_inversor == "4":  # Vender acciones
                        print("\nLista de acciones disponibles:")
                        inversor.portafolio.listar_portafolio()
                        id=int(input("Ingrese el numero de id de la accion que quiere vender: "))
                        cantidad= int(input("Ingrese la cantidad de acciones que desea vender: "))
                        inversor.portafolio.vender(id, cantidad)
                    elif opcion_inversor == "5":  # Cerrar sesión
                        print("Cerrando sesión...")
                        break
                    else:
                        print("Opción no válida. Inténtalo de nuevo.")
            else:
                print("Email o contraseña incorrectos.")
        
        elif opcion == "2":  # Registrar un nuevo usuario
            nombre = input("Introduce tu nombre: ")
            apellido = input("Introduce tu apellido: ")
            cuil = input("Introduce tu CUIL: ")
            email = input("Introduce tu email: ")
            contrasena = input("Introduce tu contraseña: ")
            Inversor.registrar_nuevo_inversor(nombre, apellido, cuil, email, contrasena)

        elif opcion == "3":  # Salir del sistema
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    iniciar()