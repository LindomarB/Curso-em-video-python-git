# criar um programa para ler o valor digitado e convertelo em dolares
## considerando 1 usd = 3.27 R$

merreca = float(input('digite quantos reais vc tem seu arrombado:  '))
print('voce tem R$ {} voce pode comprar {:.2f} dolares'.format(merreca, merreca/3.27))
