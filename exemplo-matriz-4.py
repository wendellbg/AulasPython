#Criar uma matriz vazia
turma = []
#laço para criar as linhas vazias
for i in range(3):
	linha = []
	#laço para criar as colunas 
	for j in range(5):
		#Vai adicionando as notas em cada linha x coluna
		linha.append(int(input('Digite a nota [Linha '+str(i) +', Coluna ' + str(j) +']:')))
	#adiciona a linha na matriz	
	turma.append(linha)
	print(turma)
	
	
