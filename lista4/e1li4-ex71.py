# Faça um Programa que leia 5 números inteiros, armazene-os em uma lista. 
lista = []
for i in range (5):
    num = input('Digite um numero inteiro: ')
    while num.isalpha():
        num = input('Erro, numero inválido. Digite um numero inteiro: ')
    int(float)
    lista.append(num)
print(lista)