import mysql.connector

meu_banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "tioROY@2022",
    database = "banco_python"
)

meu_cursor = meu_banco.cursor()

sql = "INSERT INTO contatos (nome, telefone) VALUES (%s, %s)"
valores = ("Wendell Bento Geraldes", "62994976308")

meu_cursor.execute(sql, valores)

meu_banco.commit()

print(meu_cursor.rowcount, "Registro inserido com sucesso!")


