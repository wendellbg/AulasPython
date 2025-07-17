# ---------------------------------------
# Exercício 1 - Lista 04 - 10/07/2025
# Aluno: Wendell Bento Geraldes
# ---------------------------------------
contador = 0 #criei um contador
total = 0 #criei o total
# Enquanto o contador não chegar a 15 faça
while contador < 15:
    # Peça para o usuário digitar um numero
    soma = float(input("Digite o numero: "))
    # A variável contador recebe ela mesma + 1
    contador += 1
    # A variável total recebe ela mais a cada
    # numero digitado e soma
    total += soma
    print(f"A variável total tem {total}")
print(f"A soma dos {15} números é ",total)
    
 
    
    