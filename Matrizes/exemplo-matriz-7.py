linhas = int(input('Digite a quantidade de linhas da matriz: '))
colunas = int(input('Digite a quantidade de colunas da matriz: '))
matriz = []
for i in range(linhas):  
    matriz.append([0]*colunas)
for i in range(linhas):
    print(matriz[i])