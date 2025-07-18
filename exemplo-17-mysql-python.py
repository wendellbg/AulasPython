import mysql.connector

meu_banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "tioROY@2022",
    database = "banco_python"
)

meu_cursor = meu_banco.cursor()

sql = "DELETE FROM contatos WHERE nome = 'Wendell Bento Geraldes'"

meu_cursor.execute(sql)

meu_banco.commit()

print(meu_cursor.rowcount, "Registro excluído com sucesso!")

