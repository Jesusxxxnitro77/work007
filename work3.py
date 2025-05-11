import random

numeros = random.sample(range(1, 101), 100)

pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

for i in range(len(impares)):
    for j in range(len(impares) - 1):
        if impares[j] > impares[j + 1]:
            temp = impares[j]
            impares[j] = impares[j + 1]
            impares[j + 1] = temp

print("Números impares ordenados de menor a mayor:")
for num in impares:
    print(num)

