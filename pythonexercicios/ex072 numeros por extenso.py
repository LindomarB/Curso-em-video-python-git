#Exercício Python 072: Crie um programa que tenha uma dupla totalmente
# preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20)
#  e mostrá-lo por extenso.#
numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'set',
          'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze',
          'quinze', 'dezaseis', 'dezasete', 'dezoito', 'dezanove', 'vinte')
while True:
    n = int(input('digite um numero 0-20: '))
    if 0 <= n <= 20:
        print('voce digitou o numero {}'.format(numero[n]))
        resp = ''
        resp = str(input('quer continuar ? s/n: ')).upper().strip()
        while resp not in 'S/N':
            resp = str(input('quer continuar ? s/n: ')).upper().strip()
        if resp == 'N':
            break
