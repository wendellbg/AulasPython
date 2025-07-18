import mysql.connector

meu_banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "tioROY@2022",
    database = "banco_python"
)

meu_cursor = meu_banco.cursor()

sql = "INSERT INTO contatos (nome, telefone) VALUES (%s, %s)"
valores = ("William Bento Geraldes", "62999997777")

meu_cursor.execute(sql, valores)

meu_banco.commit()

print("1 Registro(s) inserido com sucesso, com o ID: ",meu_cursor.lastrowid)


