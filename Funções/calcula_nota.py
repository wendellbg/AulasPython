import funcoes

nota1 = funcoes.ler_notas()
nota2 = funcoes.ler_notas()
nota3 = funcoes.ler_notas()
nota4 = funcoes.ler_notas()

resultado = funcoes.calcula_media(nota1, nota2, nota3, nota4)

print("A média do aluno é: ",resultado)

funcoes.verifica_aprovacao(resultado)