#faça um programa que leia se um ano
#e mostre se ele é bissexto

from datetime import date
ano = int(input('digite o ano .. para o ano atual digiete 0:'))
if ano == 0:
    ano = date.today().year
if ano  % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o {} é ano bissexto'.format(ano))
else:
    print('o ano {} nao é bissexto'.format(ano))