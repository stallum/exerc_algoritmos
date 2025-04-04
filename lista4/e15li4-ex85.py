# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma.

windowsServers = []
unix = []
linux = []
netware = []
macOs = []
outros = []
num = 1

print('Qual o melhor Sistema Operacional para uso em servidores?')
print('As possíveis respostas são: \n1 - Windows Servers \n2 - Unix \n3 - Linux\n4 - Netware\n5 - Mac Os\n6 - Outros')

while num > 0:
    num = input('\033[mDigite sua resposta para a enquete (ou 0 para termina-la): ')
    while num.isalpha() or int(num) > 6:
        num = input('\033[1;31mERRO. Digite uma resposta válida: ')
    num = int(input)

    if num == 1:
        windowsServers.append(num)
    else:
        if num == 2:
            unix.append(num)
        else:
            if num == 3:
                linux.append(num)
            else:
                if num == 4:
                    netware.append(num)
                else: 
                    if num == 5:
                        macOs.append(num)
                    else:
                        if num == 6:
                            outros.append(num)
    