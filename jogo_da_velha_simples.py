tabuleiro = [" "] * 9
jogador = "X"
jogadas = 0
placar = {"X": 0, "O": 0}

while True:
    # Exibir o tabuleiro
    print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
    print("--+---+--")
    print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
    print("--+---+--")
    print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")
    
    # Jogada do usuário
    try:
        pos = int(input(f"Jogador {jogador}, escolha uma posição (1-9): ")) - 1
        if tabuleiro[pos] != " " or pos not in range(9):
            print("Posição inválida. Tente novamente.")
            continue
    except (ValueError, IndexError):
        print("Entrada inválida. Use números de 1 a 9.")
        continue
    
    tabuleiro[pos] = jogador
    jogadas += 1
    
    # Verificar vitória
    combinacoes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # colunas
        [0, 4, 8], [2, 4, 6]              # diagonais
    ]
    ganhou = False
    for combo in combinacoes:
        if tabuleiro[combo[0]] == tabuleiro[combo[1]] == tabuleiro[combo[2]] == jogador:
            ganhou = True
            break
    if ganhou:
        print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
        print("--+---+--")
        print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
        print("--+---+--")
        print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")
        print(f"Jogador {jogador} venceu!")
        placar[jogador] += 1
        print(f"Placar: X = {placar['X']} | O = {placar['O']}")
        if input("Jogar novamente? (s/n): ").lower() != "s":
            break
        tabuleiro = [" "] * 9
        jogadas = 0
        jogador = "X"
        continue
    
    if jogadas == 9:
        print("Empate!")
        print(f"Placar: X = {placar['X']} | O = {placar['O']}")
        if input("Jogar novamente? (s/n): ").lower() != "s":
            break
        tabuleiro = [" "] * 9
        jogadas = 0
        jogador = "X"
        continue
    
    jogador = "O" if jogador == "X" else "X"