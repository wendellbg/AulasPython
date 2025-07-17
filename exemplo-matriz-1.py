def constroiMatriz1():
	#Cria uma matriz vazia
	matriz = []
	for i in range(4):
		# Cada vez que o laço for i in range(4)
        # passar por aqui ele vai criar uma linha vazia
		linha = []
		for j in range(3):
			# Cada vez que o laço for j in range(3)
            # passar por aqui ele vai adicionar um zero na linha e coluna
			list.append(linha, 0)
			matriz = matriz + [linha]
	return matriz
print(constroiMatriz1())
    