def soma2numeros(x, y):     
    soma = x + y
    return soma

def soma3numeros(a, b, c):
    return a + b + c

def somaImposto(taxaImposto, custo):    
    taxaImposto = (taxaImposto / 100)   
    valor_imposto = (custo * taxaImposto)
    preco_com_imposto = (custo + valor_imposto)
    return preco_com_imposto

def moldura(palavra):
    print("+--------------+")
    print("|"+"   "+palavra+"   "+"|")
    print("+--------------+")
        
    
    