# importando biblioteca matemática para a função de 
# raiz quadrada
import math

# Inserindo coordenadas dos pontos
xA = float(input("Digite a abscissa do ponto A: "))
xB = float(input("Digite a abscissa do ponto B: "))
yA = float(input("Digite a ordenada do ponto A: "))
yB = float(input("Digite a ordenada do ponto B: "))

# Calculando a distância
distAB = math.sqrt(((xA-xB)**2)+((yA-yB)**2))

# Mostando resultado
print("A distância entre esses dois pontos é de: ",distAB,"unidades de medida")
