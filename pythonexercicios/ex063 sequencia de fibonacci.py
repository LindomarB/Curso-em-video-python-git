#Escreva um programa que leia um número N inteiro qualquer #
# #e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. #
print('seguencia de finobacci')
print('=-='*20)
n = int(input('quantos termos da seguencia de fibonaci vc deseja mostrar ?: '))
t1 = 0
t2 = 1
cont = 3
print('=-='*20)
print('{} ->{}'.format(t1, t2), end='')
while cont <= n:
    t3 = t1 + t2
    print(' ->', t3, end='')
    t1 = t2
    t2 = t3
    cont += 1
print('\nFim')
