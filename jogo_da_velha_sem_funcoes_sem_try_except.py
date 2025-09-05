# Jogo da Velha sem funções e sem try/except

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

    entrada = input(f"Jogador {jogador}, escolha uma posição (1-9): ")
    if not entrada.isdigit():
        print("Por favor, digite um número de 1 a 9.")
        continue

    pos = int(entrada) - 1
    if pos not in range(9):
        print("Posição fora do tabuleiro. Tente novamente.")
        continue

    if tabuleiro[pos] != " ":
        print("Posição já ocupada. Escolha outra.")
        continue

    tabuleiro[pos] = jogador
    jogadas += 1

    # Verifica vitória
    ganhou = False
    # Combinações possíveis
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