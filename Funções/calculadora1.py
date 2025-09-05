# Calculadora básica versão 1.0
# Autor: Wendell
# Data: 05 de setembro de 2025

# Menu da calculadora
canto_superior_esquerdo = chr(9484)  # a função chr serve para mostrar esse caraceter ┌
canto_superior_direito = chr(9488)   # a função chr serve para mostrar esse caraceter ┐
canto_inferior_esquerdo = chr(9492)  # a função chr serve para mostrar esse caraceter └
canto_inferior_direito = chr(9496)   # a função chr serve para mostrar esse caraceter ┘
horizontal = chr(9472)               # a função chr serve para mostrar esse caraceter ─
vertical = chr(9474)                 # a função chr serve para mostrar esse caraceter │
    

# linha superior
print(canto_superior_esquerdo + horizontal * int(38) + canto_superior_direito)
print(vertical + "Escolha a operação que deseja realizar" + vertical)
print(vertical + "Digite 1 para Soma                    " + vertical)
print(vertical + "Digite 2 para Subtração               " + vertical)
print(vertical + "Digite 3 para Multiplicação           " + vertical)
print(vertical + "Digite 4 para Divisão                 " + vertical)
print(vertical + "Digite 0 para Sair                    " + vertical)
# linha inferior
print(canto_inferior_esquerdo + horizontal * int(38) + canto_inferior_direito)

# selecionado a opção e realizando a operação desejada
operacao = int(input("Informe o número da operação: "))
if operacao == 1:
    print("Você escolheu Somar")
    numero1 = int(input("Informe o primeiro número: "))
    numero2 = int(input("Informe o segundo número: "))
    resultado = numero1 + numero2
    print("O resultado é: ",resultado)
elif operacao == 2:
    print("Você escolheu Subtrair")
    numero1 = int(input("Informe o primeiro número: "))
    numero2 = int(input("Informe o segundo número: "))
    resultado = numero1 - numero2
    print("O resultado é: ",resultado)
elif operacao == 3:
    print("Você escolheu Multiplicar")
    numero1 = int(input("Informe o primeiro número: "))
    numero2 = int(input("Informe o segundo número: "))
    resultado = numero1 * numero2
    print("O resultado é: ",resultado)
elif operacao == 4:
    print("Você escolheu Dividir")
    numero1 = int(input("Informe o primeiro número: "))
    numero2 = int(input("Informe o segundo número: "))
    resultado = numero1 / numero2
    print("O resultado é: ",resultado)
elif operacao == 0:
    print("Você escolheu Sair, obrigado por usar a nossa calculadora")    
elif operacao < 0 or operacao > 4:
    print("Esta operação é inválida")
    
    