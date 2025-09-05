import mysql.connector

meu_banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "tioROY@2022",
    database = "banco_python"
)

meu_cursor = meu_banco.cursor()

sql = "SELECT * FROM contatos WHERE nome = %s"
criterio = ("William Bento Geraldes",)

meu_cursor.execute(sql, criterio)

resultado = meu_cursor.fetchall()

for x in resultado:
    print(x)


