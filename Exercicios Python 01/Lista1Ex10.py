# 10. O corac˜ao humano bate em m´edia uma vez por
# segundo. Desenvolva um algoritmo para calcular
# e escrever quantas vezes o cora¸c˜ao de uma pessoa bater´a se viver X anos. Dado de
# entrada: idade da pessoa (inteiro em anos).
# Considera¸c˜oes: 1 ano = 365,25 dias,
# 1 dia = 24 horas, 1 hora = 60 minutos
# e 1 minuto = 60 segundos.
idade=int(input("Informe a sua idade:"))
batidas=idade*365.25*24*60*60
print("A quantidade de batidas do seu coração é ",batidas)
