# Inicializando a lista vazia para armazenar os números
numeros = []

# Lendo os 20 números inteiros
for i in range(20):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)    

# Calculando a soma dos números
soma = sum(numeros)

# Calculando a média aritmética
#media = soma / len(numeros)
media = soma / 20

# Exibindo o resultado
print(f"A média aritmética dos números é: {media}")
