# 19.	Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais elementos. Escreva ao ﬁnal a matriz obtida.

# matriz = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9,], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]
matriz = []
for i in range(5):
    linha = []
    for j in range(5):
        valor = input(f'Digite o valor para a posição [{i}][{j}]: ')
        linha.append(valor)
    matriz.append(linha)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i == j:
            matriz[i][j] = 1
        else: 
            matriz[i][j] = 0

for x in range(len(matriz)):
    print(matriz[x])