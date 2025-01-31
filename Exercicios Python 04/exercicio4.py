with open("anotacoes.txt", "r") as arquivo:
    contador = 0
    for linha in arquivo:
        contador += 1
print("O número de linhas no arquivo é:",contador)