#Crie um programa que leia vários números inteiros pelo teclado.#
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. #
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.#
soma = cont = media = maior = menor = 0
resp = 'Ss'
while resp in 'Ss':
    num = int(input('digite um numero: '))
    soma += num
    cont += 1
    if cont == 1: # se o numero e o primeiro digitado esse valor recebe o maior e menor valor#
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar ?:[S/N]')).strip()[0]
media = soma/ cont
print(' a soma é {}  a media {} o maior numero é {} e o menor {} dos {} valores digitados'. format( soma, media, maior, menor , cont))