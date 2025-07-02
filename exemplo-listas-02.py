#Exemplo de uso de listas no Python
notas = []
qtde_notas = int(input("Informe a quantidade de notas que vai digitar: "))
i = 1
while i <= qtde_notas:
    nota = float(input(f"Digite a nota {i}: "))
    i = i + 1
    notas.append(nota)
    
soma_notas = 0
for nota in notas:
    soma_notas += nota

media = soma_notas / qtde_notas
print("A média das notas é: ",media)

