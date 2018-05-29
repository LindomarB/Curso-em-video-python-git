# faça um programa que leia o comprimento
# do cateto adjacento o cateto oposto de um triangulo retangulo
# calcule e mostre o comprimento da hipotenusa
from math import sqrt
a = float(input('digite o valor do cateo oposto '))
b = float(input('digite o valor do cateto adjacente '))
hi = (a**2 + b**2)
print('o valor da hipotenusa é {:.2f}'.format(sqrt(hi)))
