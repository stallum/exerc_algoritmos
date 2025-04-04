# Faça um Programa que leia e armazene 50 números inteiros, mostre a soma, a multiplicação e os números. 
numeros = []
soma = 0
multiplicacao = 1

for i in range(50):
    num = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(num)
    soma += num
    multiplicacao *= num

print("\nNúmeros digitados:", numeros)
print("Soma dos números:", soma)
print("Multiplicação dos números:", multiplicacao)
