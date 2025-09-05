# Jogo da Velha sem funções, mas com try/except

tabuleiro = [" "] * 9
jogador = "X"
jogadas = 0
placar = {"X": 0, "O": 0}

while True:
    print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
    print("--+---+--")
    print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
    print("--+---+--")
    print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")

    try:
        pos = int(input(f"Jogador {jogador}, escolha uma posição (1-9): ")) - 1
        if tabuleiro[pos] != " " or pos not in range(9):
            print("Posição inválida ou já ocupada. Tente novamente.")
            continue
    except (ValueError, IndexError):
        print("Entrada inválida. Use números de 1 a 9.")
        continue

    tabuleiro[pos] = jogador
    jogadas += 1

    # Verifica vitória
    ganhou = False
    if (tabuleiro[0] == tabuleiro[1] == tabuleiro[2] == jogador) or \
       (tabuleiro[3] == tabuleiro[4] == tabuleiro[5] == jogador) or \
       (tabuleiro[6] == tabuleiro[7] == tabuleiro[8] == jogador) or \
       (tabuleiro[0] == tabuleiro[3] == tabuleiro[6] == jogador) or \
       (tabuleiro[1] == tabuleiro[4] == tabuleiro[7] == jogador) or \
       (tabuleiro[2] == tabuleiro[5] == tabuleiro[8] == jogador) or \
       (tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == jogador) or \
       (tabuleiro[2] == tabuleiro[4] == tabuleiro[6] == jogador):
        ganhou = True

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
        print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
        print("--+---+--")
        print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
        print("--+---+--")
        print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")
        print("Empate!")
        print(f"Placar: X = {placar['X']} | O = {placar['O']}")
        if input("Jogar novamente? (s/n): ").lower() != "s":
            break
        tabuleiro = [" "] * 9
        jogadas = 0
        jogador = "X"
        continue

    jogador = "O" if jogador == "X" else "X"