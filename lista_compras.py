lista_compras = []

while True:
    item = input("Digite um item para adicionar à lista de compras (ou 'sair' para finalizar): ")
    if item == 'sair':    
        break
    #Append inclui um item na lista    
    lista_compras.append(item)

print("\nSua lista de compras:")
for item in lista_compras:
    print(item)