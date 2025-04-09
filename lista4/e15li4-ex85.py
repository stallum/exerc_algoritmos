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
    num = int(num)

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
totalVotos = len(windowsServers) + len(unix) + len(linux) + len(netware) + len(macOs) + len(outros)

print('Tabela de Resultados da Enquete'.center(45))
print(f'Sistema Operacional {'Votos':<15} {'%':<25}')
print(f'------------------- {'---------------'} {'---------------'}')
print(f'{'Windows Servers                 '} {len(windowsServers):<12} {(len(windowsServers) / totalVotos) * 100:.2f}')
print(f'{'Unix                            '} {len(unix):<12} {(len(unix) / totalVotos) * 100:.2f}')
print(f'{'Linux                           '} {len(linux):<12} {(len(linux) / totalVotos) * 100:.2f}')
print(f'{'Netware                         '} {len(netware):<12} {(len(netware) / totalVotos) * 100:.2f}')
print(f'{'Mac OS                          '} {len(macOs):<12} {(len(macOs) / totalVotos) * 100:.2f}')
print(f'{'Outros                          '} {len(outros):<12} {(len(outros) / totalVotos) * 100:.2f}')

if len(windowsServers) > len(unix) and len(windowsServers) > len(linux) and len(windowsServers) > len(netware) and len(windowsServers)> len(macOs) and len(windowsServers) > len(outros): 
    print(f'O sistema operacional mais votado foi o Windows Servers, com {len(windowsServers)} votos, que corresponde a: {(len(windowsServers) / totalVotos) * 100:.2f}% dos votos') 

if len(unix) > len(windowsServers) and len(unix) > len(linux) and len(unix) > len(netware) and len(unix)> len(macOs) and len(unix) > len(outros): 
    print(f'O sistema operacional mais votado foi o Windows Servers, com {len(unix)} votos, que corresponde a: {(len(unix) / totalVotos) * 100:.2f}% dos votos') 

if len(linux) > len(unix) and len(linux) > len(windowsServers) and len(linux) > len(netware) and len(linux)> len(macOs) and len(linux) > len(outros): 
    print(f'O sistema operacional mais votado foi o Windows Servers, com {len(linux)} votos, que corresponde a: {(len(linux) / totalVotos) * 100:.2f}% dos votos') 

if len(netware) > len(unix) and len(netware) > len(linux) and len(netware) > len(windowsServers) and len(netware)> len(macOs) and len(netware) > len(outros): 
    print(f'O sistema operacional mais votado foi o Windows Servers, com {len(linux)} votos, que corresponde a: {(len(linux) / totalVotos) * 100:.2f}% dos votos') 

if len(macOs) > len(unix) and len(macOs) > len(linux) and len(macOs) > len(netware) and len(macOs)> len(windowsServers) and len(macOs) > len(outros): 
    print(f'O sistema operacional mais votado foi o Windows Servers, com {len(linux)} votos, que corresponde a: {(len(linux) / totalVotos) * 100:.2f}% dos votos') 

if len(outros) > len(unix) and len(outros) > len(linux) and len(outros) > len(netware) and len(outros) > len(macOs) and len(outros) > len(windowsServers): 
    print(f'O sistema operacional mais votado foi o Windows Servers, com {len(linux)} votos, que corresponde a: {(len(linux) / totalVotos) * 100:.2f}% dos votos') 