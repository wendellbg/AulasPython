nomes = ["Augusto", "Francisco", "Maria", "Eduardo", "Elaine", "Marcos"]
notas = [10, 5.5, 4.3, 7.2, 8.0, 9.5]
#Media da turma
soma = 0
for nota in notas:
    soma += nota
    media = soma/len(notas)
print("A média da turma é: ",round(media,2))
# Verificar qual o aluno está acima da média da turma e qual está
# abaixo da média da turma
for i in range(len(notas)):
    if notas[i] > media:
        print("Aluno com nota acima da media: ", nomes[i])        
    else:
        print("Aluno com nota abaixo da media: ", nomes[i])