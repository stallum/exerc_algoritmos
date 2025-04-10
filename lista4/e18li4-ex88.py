# 18.	Leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela possui. 

# matriz = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

matriz = []
for i in range(4):
    linha = []
    for j in range(4):
        valor = input(f'Digite o valor para a posição [{i}][{j}]: ')
        while valor.isalpha():
            valor = input('o valor digitado é inválido, digite um valor numerico: ')
        valor = float(valor)
        linha.append(valor)
    matriz.append(linha)

count = 0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] > 10:
            count += 1

print(f'Existem {count} valores maiores que 10 nessa matriz.')