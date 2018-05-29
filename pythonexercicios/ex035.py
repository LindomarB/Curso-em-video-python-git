##desenvolva um programa que leia 3 retas e diga ao usuario
##se els podem ou nao formar um triangulo



##pesquisar 3 retas pra formar um triangulo calculo matematico


a = float(input('digite um numero: '))
b = float(input('digite outro numero: '))
c = float(input('digite um terceiro numero: '))

if a < b + c and b < a + c and c < a + b:
    print(' forma um triangulo ')

else:
    print('estas medidas nao formam um triangulo')
