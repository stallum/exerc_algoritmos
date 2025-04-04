# 16. Escreva um programa em Python para encontrar o segundo maior elemento de uma lista com 20 números inteiros. 
# 
# OBS: todos os valores informados serão de valores diferentes e a solução não deve fazer este tratamento das entradas. Além disso, a solução não deve modificar a lista original com a ordem fornecida dos números.

numeros = []
'''
for i in range(20):
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)

maior = None
segundo_maior = None

i = 0
while i < len(numeros):
    if maior is None or numeros[i] > maior:
        segundo_maior = maior  
        maior = numeros[i]  
    elif segundo_maior is None or numeros[i] > segundo_maior:
        segundo_maior = numeros[i] 
    i += 1

print(f"O segundo maior número é: {segundo_maior}")
'''

'''
entrada = input('Digite os 20 numeros que você quer conferir o segundo maior: ')
numeros = entrada.split()

lista = [float(num) for num in numeros]

maior = None
segundo_maior = None

i = 0
while i < len(lista):
    if maior is None or lista[i] > maior:
        segundo_maior = maior  
        maior = lista[i]  
    elif segundo_maior is None or lista[i] > segundo_maior:
        segundo_maior = lista[i] 
    i += 1

print(f"O segundo maior número é: {segundo_maior}")
'''

entrada = input('Digite os 20 numeros que você quer conferir o segundo maior: ')
numeros = entrada.split()
lista = [float(entrada) for entrada in numeros]

lista.sort()
segundoMenorNumero = lista[-2]
print(f'o segundo maior numero é: {segundoMenorNumero}')
print(numeros)
print(lista)