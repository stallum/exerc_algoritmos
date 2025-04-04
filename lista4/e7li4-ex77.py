# Faça um Programa que peça a idade e a altura de 10 pessoas, armazene cada informação na sua respectiva lista. Imprima a idade da pessoa que possui maior altura.

idades = []
alturas = []

for i in range(10):
    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))
    altura = float(input(f"Digite a altura da pessoa {i + 1} (em metros): "))
    idades.append(idade)
    alturas.append(altura)

maior_altura = max(alturas)
indice_maior_altura = alturas.index(maior_altura)
print(f"A idade da pessoa com maior altura ({maior_altura}m) é: {idades[indice_maior_altura]}")