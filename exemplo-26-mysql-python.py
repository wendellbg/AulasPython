import mysql.connector

meu_banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "tioROY@2022",
    database = "banco_python"
)


listagem = input("Deseja ver uma listagem dos contatos, digite s(SIM) ou n(NÃO): ")
if listagem == "s":
    ordem = input("Deseja ver a listagem em ordem crescente de nome?, digite s(SIM) ou n(NÃO): ")
    if ordem == "s":
        meu_cursor = meu_banco.cursor()
        sql = "SELECT * FROM contatos ORDER BY nome"
        meu_cursor.execute(sql)
        resultado = meu_cursor.fetchall()
        for x in resultado:
            print(x)
    else:
        meu_cursor = meu_banco.cursor()
        sql = "SELECT * FROM contatos"
        meu_cursor.execute(sql)
        resultado = meu_cursor.fetchall()
        for x in resultado:
            print(x)
elif listagem == "n":
    print("Obrigado e até breve")
    
    