# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos. 
idades = []
alturas = []
mediaAltura = 0
count = 0

for i in range(3):

    idade = input(f'\033[0;32mDigite sua idade: ')
    while idade.isalpha() or int(idade) < 0:
        idade = input(f'\033[0;31mERRO, digite uma idade válida: ')
    idade = int(idade)

    idades.append(idade)

    altura = input(f'\033[0;32mDigite sua altura: ')
    while altura.isalpha() or float(altura) < 0:
        altura = input(f'\033[0;31mDigite uma altura válida: ')
    altura = float(altura)

    if altura < 100: 
        altura = altura * 100
    
    alturas.append(altura)
    mediaAltura = sum(alturas) / len(alturas)

    if idade > 13 and altura > mediaAltura:
        count += 1

print(f'\033[0mNessa turma tem: {count} alunos maiores de 13 anos e com altura maior a média ({mediaAltura / 100:.2f} m) da sala.')
