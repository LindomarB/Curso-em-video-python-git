##programa que leia um número de 0 a 9999 e
# mostre na tela cada um dos dígitos separados

num = str(input('Digite um numero de 0 a 9999: ')).zfill(4)
print(len(num))
print('milhar {}'.format(num[0:1]))
print('centena {}'.format(num[1:2]))
print('dezena {}'.format(num[2:3]))
print('unidade {}'.format(num[3:4]))
