from src.usuarios.usuarios import Usuario

def login(usuario, contraseña):
    id_usuario = Usuario.es_usuario_valido(usuario, contraseña)
    if id_usuario:
        return id_usuario
    else: return False