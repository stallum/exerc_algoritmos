# Faça um Programa que leia três listas com 10 elementos cada. Gere uma quarta lista de 30 elementos, cujos valores deverão ser compostos pelos elementos intercalados das duas outras listas. 

lista1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
lista2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]
lista3 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
lista4 = []

for i in range (len(lista1)):
    lista4.append(lista1[i])
    lista4.append(lista2[i])
    lista4.append(lista3[i])
print(lista4)