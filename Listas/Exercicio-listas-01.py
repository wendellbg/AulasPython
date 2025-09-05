# Calcule a média de quatro notas de
# um(a) aluno(a) e mostre na tela se ele(ela)
# está aprovado(a) ou reprovado(a)

nota1 = float(input("Informe a nota 1: "))
nota2 = float(input("Informe a nota 2: "))
nota3 = float(input("Informe a nota 3: "))
nota4 = float(input("Informe a nota 4: "))
media = (nota1 + nota2 + nota3 + nota4)/4
print("A média do(a) aluno(a) é: ",media)
if media < 6:
    print("O(a) aluno(a) está reprovado(a)")
else:
    print("O(a) aluno(a) está aprovado(a)")