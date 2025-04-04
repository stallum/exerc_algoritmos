# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numa lista a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0

medias = []

for i in range(3):
    notas = []
    for i in range(4):
        nota = input(f'Digite sua {i + 1 }ª nota: ')
        while nota.isalpha():
            nota = input('Erro, digite uma nota válida: ')
        nota = float(nota)
        notas.append(nota)
    media = sum(notas) / len(notas)
    medias.append(media)

print("Médias maiores ou iguais a 7.0:")
for media in medias:
    if media >= 7.0:
        print(media)
