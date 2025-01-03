import funcoes

preco_custo = float(input("Digite o preço de custo: "))
taxa = float(input("Digite o valor do Imposto: "))
print("O preço de venda é: ", funcoes.somaImposto(taxa, preco_custo)) 

