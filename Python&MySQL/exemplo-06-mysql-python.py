import mysql.connector

meu_banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "tioROY@2022",
    database = "banco_python"
)

meu_cursor = meu_banco.cursor()

meu_cursor.execute("ALTER TABLE contatos ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")


