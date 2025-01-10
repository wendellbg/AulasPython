# Funções para o gerenciamento de tarefas
def adicionar_tarefa(tarefas):
    tarefa = input("Digite a tarefa a ser adicionada: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def listar_tarefas(tarefas):
    if len(tarefas) == 0:
        print("Não há tarefas no momento.")
    else:
        print("\nTarefas:")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")

def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa que deseja remover: "))
        if 1 <= indice <= len(tarefas):
            tarefas.pop(indice - 1)
            print("Tarefa removida com sucesso!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, insira um número válido.")

def menu():
    tarefas = []  # Lista de tarefas
    while True:
        print("\n--- Gerenciador de Tarefas ---")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Remover tarefa")
        print("4. Sair")
        
        opcao = input("Escolha uma opção (1-4): ")
        
        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            remover_tarefa(tarefas)
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida, por favor escolha uma opção entre 1 e 4.")

# Chamada da função de menu para rodar o programa
menu()
