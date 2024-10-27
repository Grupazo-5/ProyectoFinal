import mysql.connector

def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="2291",
        database="broker_ispc"
    )
    

