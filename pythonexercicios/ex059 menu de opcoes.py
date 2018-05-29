#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.##
escolha = 0
n1 = int(input('digite um numero: '))
n2 = int(input('digite um segundo valor: '))

print('''[1] somar
[2] multiplicar
[3] maior
[4] novos m]numeros
[5] sair do programa''')
while escolha != 5:
    escolha = int(input('qual a sua opçao: '))

    if escolha == 1:
        print('{}'.format(n1 + n2))
    elif escolha == 2:
        print('{}'. format(n1 * n2))
    elif escolha == 3:
        if n1 > n2:
            print('{} e o maior valor digitado'.format(n1))
        if n2 > n1:
            print('{} e o maior valor digitado'.format(n2))
    elif escolha == 4:
        print('digite novos valores')
        n1 = int(input('digite um numero: '))
        n2 = int(input('digite um segundo valor: '))
    elif escolha == 5:
        print('saindo....')
    else:
        print(' escolha invalida')

print('Fim do programa,Volte sempre')