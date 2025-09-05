#Exemplo de listas no Python
#Calculando a média de um aluno com uma lista de notas
notas = [10, 5.5, 6.5, 3.8]
soma_notas = 0
qtde_notas = len(notas)
for nota in notas:
    soma_notas += nota

media = soma_notas / qtde_notas
print(media)