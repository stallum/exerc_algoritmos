# Faça um Programa que leia uma lista A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor. 

A = []
soma = 0

for i in range(10):
    num = input('Digite um número inteiro: ')
    while num.isalpha(): 
        num = input('Erro, digite um numero inteiro válido: ')
    num = int(num)
    quadrado = num ** 2
    soma += quadrado

print(soma)
