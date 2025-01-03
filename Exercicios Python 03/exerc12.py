perg1 = int(input("Você telefonou para a vítima? (Sim = 1/Não = 0): "))
perg2 = int(input("Você esteve no local do crime? (Sim = 1/Não = 0): "))
perg3 = int(input("Você mora perto da vítima? (Sim = 1/Não = 0): "))
perg4 = int(input("Você devia para a vítima? (Sim = 1/Não = 0): "))
perg5 = int(input("Você já trabalhou com a vítima? (Sim = 1/Não = 0): "))
if (perg1+perg2+perg3+perg4+perg5) == 2:
    print("Você é um suspeito!")
elif (perg1+perg2+perg3+perg4+perg5) == 3 or (perg1+perg2+perg3+perg4+perg5) == 4:
    print("Você é um cúmplice!")
elif (perg1+perg2+perg3+perg4+perg5) == 5:
    print("Você é o Assassino!")
else:
    print("Você é Inocente!")