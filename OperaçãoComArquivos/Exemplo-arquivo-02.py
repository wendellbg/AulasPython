# Mostrar o conteúdo do arquivo de uma vez só
#arquivo = open('exemplo.txt', 'r')
#print(arquivo.read())
# Mostrar o conteúdo do arquivo linha por linha
with open('exemplo.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)