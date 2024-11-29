x = int(input("Digite um número de 1 a 7: "))
if x == 1:
    print("Domingo")
elif x == 2:
    print("Segunda-feira")
elif x == 3:
    print("Terça-feira")
elif x == 4:
    print("Quarta-feira")
elif x == 5:
    print("Quinta-feira")
elif x == 6:
    print("Sexta-feira")
elif x == 7:
    print("Sábado")
elif x <= 0 or x > 7:
    print("Código desconhecido")
        