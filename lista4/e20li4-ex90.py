# 20.	Leia uma matriz 5 x 5. Leia também um valor X. O programa deverá fazer uma busca desse valor na matriz e, ao ﬁnal, escrever a localizacão (linha e coluna) ou uma mensagem de “não encontrado”.

matriz = []
for i in range(5):
    linha = []
    for j in range(5):
        valor = input(f'Digite o valor para a posição [{i}][{j}]: ')
        linha.append(valor)
    matriz.append(linha)

X = input('Digite um valor para "X" para que possa ser encontrado na Matriz: ')
