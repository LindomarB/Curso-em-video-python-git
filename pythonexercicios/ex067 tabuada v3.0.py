#Faça um programa que mostre a tabuada de vários números,#
#um de cada vez, para cada valor digitado pelo usuário. #
#O programa será interrompido quando o número solicitado for negativo.
print('-='*20)
print('Tabuada v3.0')
print('-='*20)
while True:
    num = int(input('digite um numero para ver a sua taboada. Digite [0] para sair: '))
    if num == 0:
        break
    cont = 0
    while cont < 11:
        print('{} X {} = {}'.format(num, cont, num * cont))
        cont += 1