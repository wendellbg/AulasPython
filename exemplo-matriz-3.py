#Criando a matriz turma
turma = [[10.0, 7.0, 9.0, 5.5, 6.0], [8.0, 10.0, 5.0, 4.5, 5.5], [6.0, 7.0, 9.0, 5.5, 4.0]]
#calcula a media
media = 0
#use o laço for para percorrer as linhas
for i in range(3):
    #use o laço for para percorrer as colunas
    print("Aluno ", i)
    for j in range(5):
        print("Nota ",j)
        media = media + turma[i][j]
        print("Valor ",turma[i][j])
media = media / 15
print("A media das notas é ",media)