def exibir_tabuleiro(tabuleiro):
    print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
    print("--+---+--")
    print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
    print("--+---+--")
    print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")

def checar_vitoria(tabuleiro, jogador):
    combinacoes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # colunas
        [0, 4, 8], [2, 4, 6]             # diagonais
    ]
    for combo in combinacoes:
        if all(tabuleiro[pos] == jogador for pos in combo):
            return True
    return False

def jogo():
    placar = {"X": 0, "O": 0}
    while True:
        tabuleiro = [" "] * 9
        jogador = "X"
        jogadas = 0
        while True:
            exibir_tabuleiro(tabuleiro)
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
            if checar_vitoria(tabuleiro, jogador):
                exibir_tabuleiro(tabuleiro)
                print(f"Jogador {jogador} venceu!")
                placar[jogador] += 1
                break
            if jogadas == 9:
                exibir_tabuleiro(tabuleiro)
                print("Empate!")
                break
            jogador = "O" if jogador == "X" else "X"
        print(f"Placar: X = {placar['X']} | O = {placar['O']}")
        if input("Jogar novamente? (s/n): ").lower() != "s":
            break

if __name__ == "__main__":
    jogo()