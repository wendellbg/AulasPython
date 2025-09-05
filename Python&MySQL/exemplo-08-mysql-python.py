import mysql.connector

meu_banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "tioROY@2022",
    database = "banco_python"
)

meu_cursor = meu_banco.cursor()

sql = "INSERT INTO contatos (nome, telefone) VALUES (%s, %s)"
valores = [("Winston Silva Geraldes", "62999991111"),
           ("Wendyane Silva Geraldes", "62999992222"),
           ("Wilcea Pacheco Geraldes", "62999993333"),
           ("Jade Victoria Vieira Bento Geraldes", "62999994444"),
           ("Jane Vieira de Souza", "62999995555"),
           ("Cleunicea Pacheco Geraldes", "62999996666")
]

meu_cursor.executemany(sql, valores)

meu_banco.commit()

print(meu_cursor.rowcount, "Registro(s) inserido com sucesso!")


