#escreva um programa que leia um numero inteiro qualque
#e peça para o usuario escolher qual sera a base de conversao
#1 para binario
#2 para octal
#3 para hexadecimal

n = int(input('digite um numero: '))
r = int(input("""1 = binario
2 = hexadecimal
3 = octal
""" ))


if r == 1:
    print(bin(n)[2:])
elif r == 2:
    print(hex(n)[2:])
elif r == 3:
    print(oct(n)[2:])
