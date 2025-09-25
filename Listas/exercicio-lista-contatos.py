# Crie um programa para uma agenda de contatos com os
# seguintes dados: nome, telefone, e-mail
# e mostre a lista dos contatos já cadastrados

contatos = list()
continua = input("Deseja cadastrar um contato? [s/n]")
while continua == "s":
    contatos.append(input("Informe o seu nome: "))
    contatos.append(input("Informe o seu numero de telefone: "))
    contatos.append(input("Informe o seu endereço de e-mail: "))
    continua = input("Deseja continuar o cadastro? [s/n]")
    if continua == "n":
        break
for i in contatos:
    print(i)
    
    
    

    