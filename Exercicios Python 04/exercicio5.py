#Define a palavra que será pesquisada
palavra = "Python"
#Abre o arquivo em modo de leitura
with open("palavras.txt", "r") as arquivo:
	for linha in arquivo:
		#Quebra a linha em palavras separadas por espaço
		palavra_na_linha = linha.split()
		#Verifica e exibe a palavra pesquisada
		for palavra in palavra_na_linha:
			if palavra.lower() in palavra:
				print("Palavra encontrada: ",palavra)
		