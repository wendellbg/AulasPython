# um(a) aluno(a) e mostre na tela se ele(ela)
# está aprovado(a) ou reprovado(a)
# usando listas

notas = []
qtde_notas = int(input("Informe a quantidade de notas que deseja digitar: "))
contador = 0
while contador < qtde_notas:
    notas.append(float(input("Digite a nota: ")))
    contador = contador + 1
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