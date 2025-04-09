# 17.	Escreva um programa em Python para converter um número inteiro em binário de acordo com a representação de grandeza com sinal (sinal e magnitude). O programa deve receber um número inteiro e produzir como saída uma lista com os bits do número convertido (um bit para cada posição da lista). Além disso deve ser feita a verificação se o número pode ser representado, considere uma representação com 8 bits (um para o sinal e 7 para a magnitude).

for i in range(5):
    num = input('digite um numero inteiro: ')
    numBinario = []

    while num.isalpha(): 
        num = input('Erro. Valor inválido, digite um numero inteiro: ')
    num = int(num)

    if num < -255 or num > 255: 
        print('não é possível fazer essa correção para esse codigo')

    else:
        if num < 0:
            sinal = 1
            num = num * -1
        else: 
            sinal = 0

        while num > 0:
            resto = num % 2
            numBinario.append(resto)
            num = num // 2

        for i in range(7-len(numBinario)):
            numBinario.append(0)

        numBinario.append(sinal)

    numBinario.reverse()
    print(numBinario)