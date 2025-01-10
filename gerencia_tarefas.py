tarefas = []

def adicionar_tarefa(tarefa):
  #Adiciona itens do vetor
  tarefas.append(tarefa)  
  print(f"Tarefa '{tarefa}' adicionada com sucesso!")

def remover_tarefa(tarefa):
  if tarefa in tarefas:
    #Remove itens do vetor
    tarefas.remove(tarefa)
    print(f"Tarefa '{tarefa}' removida com sucesso!")
  else:
    print(f"Tarefa '{tarefa}' não encontrada.")

def listar_tarefas():
  if not tarefas:
    print("Sua lista de tarefas está vazia.")
  else:
    print("Lista de tarefas:")
    #A função enumerate retorna o indice e o elemento do vetor
    for indice, tarefa in enumerate(tarefas):
      print(f"{indice+1}. {tarefa}")

while True:
  print("\nGerenciador de Tarefas")
  print("1. Adicionar tarefa")
  print("2. Remover tarefa")
  print("3. Listar tarefas")
  print("4. Sair")

  opcao = input("Escolha uma opção: ")

  if opcao == '1':
    nova_tarefa = input("Digite a nova tarefa: ")
    adicionar_tarefa(nova_tarefa)
  elif opcao == '2':
    tarefa_remover = input("Digite a tarefa a ser removida: ")
    remover_tarefa(tarefa_remover)
  elif opcao == '3':
    listar_tarefas()
  elif opcao == '4':
    print("Saindo...")
    break
  else:
    print("Opção inválida. Tente novamente.")