import mysql.connector

meu_banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "tioROY@2022"
)

meu_cursor = meu_banco.cursor()
meu_cursor.execute("CREATE DATABASE banco_python")