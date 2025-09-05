import mysql.connector

meu_banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "tioROY@2022",
    database = "banco_python"
)

contador = 0
qtde_registros = int(input("Quantos registros você deseja inserir? "))
                
while contador < qtde_registros:
    nome = input("Informe o nome: ")
    telefone = input("Informe o número de telefone: ")
    contador += 1                     
    meu_cursor = meu_banco.cursor()
    sql = "INSERT INTO contatos (nome, telefone) VALUES (%s, %s)"
    valores = (nome, telefone)
    meu_cursor.execute(sql, valores)
    meu_banco.commit()
    print(meu_cursor.rowcount, "Registro inserido com sucesso!")


