import mysql.connector

meu_banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "tioROY@2022",
    database = "banco_python"
)

meu_cursor = meu_banco.cursor()

sql = "SELECT * FROM contatos ORDER BY nome DESC"

meu_cursor.execute(sql)

resultado = meu_cursor.fetchall()

for x in resultado:
    print(x)


