#Faça um programa que leia um número qualquer e mostre o seu fatorial.#
#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120#
###pelo modulo
###from math import factorial
###n = int(input('digite um numero para calcular o fatorial: '))
###f = factorial(n)
###print('o fatorial de {} é {}'.format(n, f))###
n = int(input('digite um numero para calcular o fatorial: '))
c = n
f = 1
print('calculando {}!='.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))