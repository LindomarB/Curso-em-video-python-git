#Faça um programa que jogue par ou ímpar com o computador.
#O jogo só será interrompido quando o jogador perder,
#mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.#
from random import randint
v = 0
while True:
    jogador = int(input('digite um numero: '))
    computador = randint(1, 10)
    total = jogador + computador
    tipo = " "
    while tipo not in 'pPIi':
        tipo = str(input('par ou impar ? [P/I]')).strip().upper()[0]
    print('voce jogou {} o computador jogou {} total {}'.format(jogador, computador, total))
    print('deu par' if total % 2 == 0 else 'deu impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('voce venceu')
            v += 1
        else:
            print('voce perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('voce venceu!')
            v += 1
        else:
            print('voce perdeu!')
            break
    print('vamos jogar novamente...')
print(f'Game Over. voce venceu {v} vezes')