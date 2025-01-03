nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1+nota2)/2
print("A sua média foi: ",media)
if media >= 0.0 and media <= 4.0:
    print("O conceito foi E")
elif media >= 4.0 and media <= 6.0:
    print("O conceito foi D")
elif media >= 6.0 and media <= 7.5:
    print("O conceito foi C")
elif media >= 7.5 and media <= 9.0:
    print("O conceito foi B")
elif media >= 9.0 and media <= 10.0:
    print("O conceito foi A")