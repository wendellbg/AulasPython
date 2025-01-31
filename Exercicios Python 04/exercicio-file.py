# Função para adicionar um novo contato ao arquivo
def adicionar_contato():
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o e-mail: ")

    # Abre o arquivo em modo de adição ('a'), para não sobrescrever os dados
    with open('contatos.txt', 'a') as arquivo:
        # Escreve as informações do contato no arquivo, separadas por vírgulas
        arquivo.write(f"{nome},{telefone},{email}\n")

    print("Contato adicionado com sucesso!\n")

# Função para exibir todos os contatos cadastrados
def exibir_contatos():
    #try inicia um tratamento de exceções e mostra o que deve ser feito
    try:
        with open('contatos.txt', 'r') as arquivo:
            #Aqui todas as linhas do arquivo serão lidas
            contatos = arquivo.readlines()

        #Se a variável contatos tiver contatos cadastrados
        if contatos:
            print("Contatos cadastrados:")
            #O laço for vai percorrer a variável mostrando todos
            #os contatos dentro do arquivo contatos.txt
            for contato in contatos:
                # Divida os dados por vírgula e exiba de forma legível
                nome, telefone, email = contato.strip().split(',')
                print(f"Nome: {nome}, Telefone: {telefone}, E-mail: {email}")
        else:
            print("Nenhum contato cadastrado ainda.\n")

    except FileNotFoundError:
        print("Nenhum contato encontrado. O arquivo 'contatos.txt' não existe.\n")

# Função principal para controlar o menu
def menu():
    #Laço while vai ficar repetindo o menu até 
    #escolher a opção 3. Sair
    while True:
        print("Bem-vindo ao Cadastro de Contatos!")
        print("Escolha uma opção:")
        print("1. Adicionar novo contato")
        print("2. Ver todos os contatos")
        print("3. Sair")

        escolha = input("Digite sua escolha: ")

        if escolha == '1':
            adicionar_contato()
        elif escolha == '2':
            exibir_contatos()
        elif escolha == '3':
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Chama a função do menu
menu()

