"""    14. Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça: 
    a. Mostre a quantidade de valores que foram lidos; 
    b. Exiba todos os valores na ordem em que foram informados
    c. Exiba todos os valores na ordem inversa à que foram informados
    d. Calcule e mostre a soma dos valores; 
    e. Calcule e mostre a média dos valores; 
    f. Calcule e mostre a quantidade de valores acima da média calculada; 
    g. Calcule e mostre a quantidade de valores abaixo de sete; 
    h. Encerre o programa com uma mensagem.
"""
nums = []
num = 0
mediaValAcima = []
notaBaixo7 = []

while num >= 0:
    num = input('Digite sua nota: (ou um numero negativo para cancelar a operação)')
    while num.isalpha() or float(num) > 10:
        num = input('Valor inválido, Digite um valor válido: (ou um numero negativo para cancelar a operação)')
    
    if num >= 0:
        nums.append(num)

print(len(nums))
print(nums)
print(nums.reverse())
print(sum(nums))
print(sum(nums)/len(nums))

for i in range(len(nums)):
    if nums[i] > (sum(nums)/len(nums)):
        mediaValAcima.append(nums[i])

print(len(mediaValAcima))

for i in range(len(nums)):
    if nums[i] < 7:
        notaBaixo7.append(nums[i])

print(len(notaBaixo7))
print('Muito obrigado por contribuir')