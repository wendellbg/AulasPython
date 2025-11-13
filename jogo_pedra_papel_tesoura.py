import random

opcoes = ["pedra", "papel", "tesoura"] # Criando um lista
jogador = input("Escolha pedra, papel ou tesoura: ").lower() # A função lower() transforme um texto em minusculas
computador = random.choice(opcoes) # random.choice escolhe uma opção aleatoriamente

print("Computador escolheu: ", computador)

if jogador == computador:
    print("Empate!")
elif (jogador == "pedra" and computador == "tesoura") or \
    (jogador == "tesoura" and computador == "papel") or \
    (jogador == "papel" and computador == "pedra"):
    print("Você acertou!")
else:
    print("Você perdeu!")
    
# Fazer uma melhor de 3 (usando um for)    