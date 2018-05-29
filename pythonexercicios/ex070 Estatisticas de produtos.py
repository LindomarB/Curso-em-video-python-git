"""Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato."""
total = totmil = menor = cont = 0
barato = ' '
while True:
    produto =str(input('nome do produto: '))
    preco = float(input('qual o preço do produto ?: '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    resp = ' '
    while resp not in 'S/N':
        resp = str(input('deseja continuar ? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'o valor total da compra foi {total} foram {totmil} produtos  acima de mil reais.'
f'\n{barato} foi o protudo de menor valor')
print('obriagado volte sempre!!')
