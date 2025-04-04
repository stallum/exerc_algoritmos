# Escreva um algoritmo que permita a leitura dos nomes de 10 pessoas  e armazene os nomes lidos em uma lista. Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de pessoa e depois escrever a mensagem ACHEI, se o nome estiver entre os 10 nomes lidos anteriormente (guardados na lista), ou NÃO ACHEI caso contrário.
nomes = []

for i in range(3):
    nome = input(f'\033[0;32mDigite o {i + 1}º nome da lista: ').lower()
    while not nome.isalpha():
        nome = input(f'\033[0;31mErro digite um nome válido (não use numeros): ').lower()
    nomes.append(nome)

nomeProcurado = input(f'\033[0m Digite um nome que você quer procurar: ').lower()

if nomeProcurado in nomes:
    print('\033[1mACHEI')
else:
    print('\033[1mNÃO ACHEI')