import mysql.connector

meu_banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "tioROY@2022",
    database = "banco_python"
)

meu_cursor = meu_banco.cursor()

meu_cursor.execute("SELECT * FROM contatos")

resultado = meu_cursor.fetchone()

print(resultado)


