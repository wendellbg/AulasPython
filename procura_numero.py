numeros = [1, 2, 3, 4, 2, 6, 7, 2, 8, 9]
valor_procurado = 2
for i in range(len(numeros)):
	if valor_procurado == numeros[i]:
		print("O número: ",int(valor_procurado)," foi encontrado")
	else:
		print("O número encontrado foi: ",i)
		