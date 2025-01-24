def menu():
       print("1 - Adiciona um novo contato")
       print("2 - Visualizar os contatos cadastrados")
       print("3 - Sair do programa")
       opcoes = int(input("Informe a opção desejada: "))
       while True:
              if opcoes == 1:
                 adiciona_contato()
              elif opcoes == 2:
                 visualiza_contato()
              elif opcoes == 3:
                 print("Sair do programa")
                 break
              else:
                 print("Opção inválida")
                 break

def adiciona_contato():
       nome = input("Informe o nome do contato: ")
       telefone = input("Informe o telefone do contato: ")
       email = input("Informe o endereço de e-mail do contato: ")
       arquivo = open("contato.txt", "a")
       arquivo.append(nome)
       arquivo.append(telefone)
       arquivo.append(email)
       
         

menu()	
