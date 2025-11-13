import random

num = random.randint(1, 10)
palpite = 0
tentativas = 0

while palpite != num:
    palpite = int(input("Adivinhe um número de 1 a 10: "))
    tentativas += 1
    if palpite < num:
        print("Muito baixo!")
    elif palpite > num:
        print("Muito alto!")
    else:
        print(f"Acertou em {tentativas} tentativas")

# Mude o intervalo (1-50) e observem o impacto