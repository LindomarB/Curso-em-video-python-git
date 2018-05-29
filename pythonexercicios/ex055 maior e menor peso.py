maior = menor = 0
for c in range(1, 6):
    peso = float(input('digite o pesso: '))
    if peso == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('o maior peso e {} e o menor é {}'.format(maior, menor))