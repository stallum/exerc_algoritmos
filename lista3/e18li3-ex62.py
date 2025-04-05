# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
"""
temp = []
num = input('Digite o número de temperaturas: ')
i = 1
while not temp.isalpha():
    temp.append(float(input(f'Digite a {i}ª temperatura: ')))
    i += 1

print(f'Menor temperatura: {min(temp)}')
print(f'Maior temperatura: {max(temp)}')
print(f'Média das temperaturas: {sum(temp) / len(temp)}')
"""

#

temp = 'começa'
temps_validas = 0
somador = 0
min_temp = None
max_temp = None

while temp != "":
    temp = input(f'\033[1;32mDigite a {temps_validas}ª temperatura (ou pressione Enter para encerrar): ')

    if temp == "":
        print('\033[1;33mFinal da Operação')

    else:
        while temp.isalpha():
            temp = input('\033[1;31mERRO, Temperatura inválida. Digite uma temperatura válida: ')
        temp = float(temp)
        somador += temp
    
        if min_temp is None or temp < min_temp:
            min_temp = temp
    
        if max_temp is None or temp > max_temp:
            max_temp = temp
        print(somador)
        temps_validas += 1
    temp = str(temp)
if temps_validas > 0:
    print(f'\033[0mMenor temperatura: {min_temp}')
    print(f'Maior temperatura: {max_temp}')
    print(f'Média das temperaturas: {somador / temps_validas}')
else:
    print('Nenhuma temperatura válida foi registrada.')