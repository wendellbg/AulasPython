# Calcule a média de quatro notas de
# um(a) aluno(a) e mostre na tela se ele(ela)
# está aprovado(a) ou reprovado(a)
# usando listas

notas = [5.5, 8.7, 3.6, 9, 6.5]
soma = 0
for item in notas:
    soma = soma + item
print("A soma é: ", soma)    
media = soma/len(notas)
print("A média é: ",media)
if media < 6:
    print("O(a) aluno(a) está reprovado(a)")
else:
    print("O(a) aluno(a) está aprovado(a)")