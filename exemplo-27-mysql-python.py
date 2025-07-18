import mysql.connector

meu_banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "tioROY@2022",
    database = "banco_python"
)


listagem = input("Deseja ver uma listagem dos contatos, digite s(SIM) ou n(NÃO): ")
if listagem == "s":
    pesquisa = input("Deseja fazer uma pesquisa por nome(N) ou telefone(T)? ")
    if pesquisa == "N":
        nome = input("Informe o nome ou parte dele: ")
        termo_pesquisa = nome
        meu_cursor = meu_banco.cursor()
        sql = f"SELECT * FROM contatos WHERE nome LIKE '%{termo_pesquisa}%'"
        meu_cursor.execute(sql)        
        resultado = meu_cursor.fetchall()
        for x in resultado:
            print(x)
    
    elif pesquisa == "T":
        telefone = input("Informe o telefone ou parte dele: ")
        termo_pesquisa = telefone
        meu_cursor = meu_banco.cursor()
        sql = f"SELECT * FROM contatos WHERE telefone LIKE '%{termo_pesquisa}%'"
        meu_cursor.execute(sql)        
        resultado = meu_cursor.fetchall()
        for x in resultado:
           print(x)
           
elif listagem == "n":
    print("Obrigado e até breve!")
    
    