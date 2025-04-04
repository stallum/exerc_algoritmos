# Faça um Programa que leia 10 números reais e mostre-os na ordem inversa.

lista = []

for i in range(3):
    num = input('Digite um numero: ') 
    while num.isalpha():
        num = input('Erro, Digite um numero válido: ')
    num = float(num)
    lista.append(num)

lista.reverse()
print(lista)
