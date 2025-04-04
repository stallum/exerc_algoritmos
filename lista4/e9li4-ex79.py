# Faça um Programa que leia duas listas com 10 elementos cada. Gere uma terceira lista de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados das duas outras listas. 

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
lista2 = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
lista3 = []

for i in range (len(lista1)):
    lista3.append(lista1[i])
    lista3.append(lista2[i])
print(lista3)