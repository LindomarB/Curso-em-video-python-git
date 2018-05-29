#faça um algoritmo que leia o preço
# de um produto e mostre seu novo preço
# com 5% DE DESCONTO


a = float(input('digite o valor do produto: '))
b = (a*5/100)
n = a - b
print('o valor do desconto de 5% do produto de valor {:.2f} é {:.2f} o valor total a ser pago é {:.2f}'.format(a, b, n))


