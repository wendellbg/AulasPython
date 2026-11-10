numero1 = int(input("Digite um numero qualquer: "))
numero2 = int(input("Digite outro numero qualquer: "))
try:
    soma = numero1 + numero2
except TypeError:
    print("Por favor, use apenas numeros para essa operação: ")
print("Obrigado por usar o nosso programa")    
    