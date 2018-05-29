##escreva um programa que faça o computador
## pensar em um numero inteiro entre 0 e 5 e peça para o usuario
##tentar descobrir qual foi o umero escolhido
## o programa devera escrever na tela se o usuario venceu opu poerdeu
#$## obs :::: vr funçao random novamente:::::
from random import randint

num = int(input('digite um numero entre 1 e 5: '))
sort = randint(1, 5)
print('o numero sorteado foi {} e o seu palpite foi {}'.format(sort, num))
if num == sort:
    print('seu palpite foi certeiro seu arrombado do caralho voce ganhou')
else:
    print('voce errou viado')
