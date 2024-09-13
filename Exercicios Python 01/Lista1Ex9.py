#9. Fazer um algoritmo que dado 4 valores
# (a, b, c, e d) calcule e escreva o valor
# das seguintes médias:
import math
a=float(input("Digite o valor de a: "))
b=float(input("Digite o valor de b: "))
c=float(input("Digite o valor de c: "))
d=float(input("Digite o valor de d: "))
m_a = (a+b+c+d)/4
m_h = 4 / ( 1/a + 1/b + 1/c + 1/d )
m_g = math.pow( a * b * c * d , 1/4)
m_q = math.sqrt( (a*a+b*b+c*c+d*d)/4 )
print("A média aritmética é ",m_a)
print("A média harmônica é ",m_h)
print("A média geométrica é ",m_g)
print("A média quadrática é ",m_q)
