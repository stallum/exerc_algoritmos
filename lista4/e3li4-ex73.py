# Faça um Programa que leia 40 notas, mostre as notas e a média na tela.

lista = []
listaMedia = []

for i in range(3):
    num = input(f'Digite sua {i + 1}ª nota: ')
    while num.isalpha():
        num = input(f'Erro numero inválido, Digite sua {i + 1}ª nota: ')
    num = float(num)
    lista.append(num)

    nota = str(num)
    listaMedia.append(nota)

    
media = (sum(lista) / len(lista))

mySep = ', '

print(f'suas notas são: {mySep.join(listaMedia)}')
print('Sua média é:', media)