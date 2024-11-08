import mysql.connector
from mysql.connector import errorcode

def conectar_db():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="broker_ispc"
        )
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuario o Password no válido")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de datos no existe.")
        else:
            print(err)
    return None