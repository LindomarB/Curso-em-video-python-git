##desenvolcva um programa que calcule a distancia de uma viagem
##em km e calcule o preço da passagem
##cobrando 0,50 por km para viagens ate 200jkm e 0,45 para viagens masi longas
valor = float(input('digite quantos km tem a viagem:'))
if valor <= 200:
    print('o valor da passagem eh de {} doletas'.format(valor*0.50))
else:
    print('o valor da passagem e de {} dolares'.format(valor*0.45))