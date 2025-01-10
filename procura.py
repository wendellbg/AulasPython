lista_carros = ["corsa", "gol", "opala", "caravan"]
valor_procurado = "opala"
for i in range(len(lista_carros)):
    if valor_procurado == lista_carros[i]:
        print("Valor procurado no indice: ", i)
    else:
        print("Não é este: ", i)