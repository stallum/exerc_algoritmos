# Faça um Programa que leia 20 números inteiros e armazene-os numa lista. Armazene os números pares na lista PAR e os números IMPARES na lista impar. Imprima as três listas. 

lista = []
listaPar = []
listaImp = []

for i in range(3):
    num = input('Digite um número inteiro: ')
    while num.isalpha() or type(num) == float:
        num = input('Digite um número inteiro válido: ')
    num = int(num)

    lista.append(num)

    if num % 2 == 0:
        listaPar.append(num)
    else: 
        listaImp.append(num)

print('total de numeros:', lista)
print('numeros impares', listaImp)
print('numeros pares', listaPar)
