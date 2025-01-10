linhas = int(input('Digite a quantidade de linhas da matriz: '))
colunas = int(input('Digite a quantidade de colunas da matriz: '))
matriz = []
for i in range(linhas):
    print("Linha: ",i)
    linha = []    
    for j in range(colunas):
        print("Coluna: ",j)
        linha.append(0)
    matriz.append(linha)
print(matriz)	