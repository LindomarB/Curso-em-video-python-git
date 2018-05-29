#Crie um programa que leia vários números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999,
#que é a condição de parada. No final, mostre quantos
#números foram digitados e qual foi a soma entre eles
#(desconsiderando o flag).#
n = cont = soma = 0
n = int(input('digite um numero [999 para sair]: '))
while n != 999:
    if n == 999:
        break
    cont += 1
    soma += n
    n = int(input('digite um numero [999 para sair]: '))
print('foram digitaos {} numeros e a soma entre eles é {}'.format(cont, soma))