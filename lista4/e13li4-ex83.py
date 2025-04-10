# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
temperaturas = []

for i in range(12):
    temperatura = input(f'Digite a média de temperatura no {i + 1} mês: ')
    while temperatura.isalpha() or float(temperatura) < 0:
        temperatura = input(f'\033[1;31mERRO, Digite uma média de temperatura válida: ')
    temperatura = float(temperatura)
    temperaturas.append(temperatura)

mediaAnual = sum(temperaturas) / len(temperaturas)

for i in range(len(temperaturas)):
    if temperaturas[i] > mediaAnual:
      print(f'A temperatura foi: {temperaturas[i]} no mês {meses[i]}')
    