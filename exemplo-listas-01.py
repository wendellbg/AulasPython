#Exemplo de listas no Python
notas = [10, 5.5, 6.5, 3.8]
soma_notas = 0
qtde_notas = len(notas)
for nota in notas:
    soma_notas += nota

media = soma_notas / qtde_notas
print(media)