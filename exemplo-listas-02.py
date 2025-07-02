#Exemplo de uso de listas no Python
#Calculando a média de um aluno com uma lista dinâmica
notas = []
qtde_notas = int(input("Informe a quantidade de notas que vai digitar: "))
i = 1
#Aqui o laço de repetição irá solicitar a digitação das notas até o limite definido na variável qtde_notas
while i <= qtde_notas:    
    nota = float(input(f"Digite a nota {i}: "))
    i = i + 1
    #Aqui usamos o append para incluir as notas digitadas pelo usuário na lista
    notas.append(nota)
    
soma_notas = 0
for nota in notas:
    soma_notas += nota

media = soma_notas / qtde_notas
print("A média das notas é: ",media)



