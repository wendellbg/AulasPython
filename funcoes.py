def ler_notas():
    nota = float(input("Digite a sua nota: "))
    return nota
            
def calcula_media(nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4)/4
    return media

def verifica_aprovacao(media):
    if media >= 6.0:
        print("O aluno foi aprovado!")
    else:
        print("O aluno foi reprovado!")