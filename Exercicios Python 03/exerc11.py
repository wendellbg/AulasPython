x = int(input("Digite a medida do primeiro lado: "))
y = int(input("Digite a medida do segundo lado: "))
z = int(input("Digite a medida do terceiro lado: "))
if x == 0 or y == 0 or z == 0:
    print("Isso não é um triângulo: ")
elif (x == y) and (x == z):
    print("Isso é um triângulo Equilátero!")
elif (x == y) or (x == z) or (y == z):
    print("Isso é um triângulo Isósceles!")
else:
    print("Isso é um triângulo Escaleno!")

   
  
