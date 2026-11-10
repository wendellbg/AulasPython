veiculo = { "marca" : "Volkswagen", "modelo": "Fusca" }
dado = input("Qual dado deseja visualizar do veículo?")
try:
    informacao_veiculo = veiculo[dado]
    print(informacao_veiculo)
except:
    print("O dado que tentou visualizar não existe no veículo")
    
print("Obrigado por utilizar o programa")
