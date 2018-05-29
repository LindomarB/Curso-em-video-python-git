##faça um programa que leia tres numeros e
##mostre qual e o maior qual e o menor

n1 = int(input('digite um numero: '))
n2 = int(input('digite o segundo numero: '))
n3 = int(input('digite o terceiro numero: '))
if n1 > n2:
    maior = n1
else:
    maior = n2
if n3 > maior:
    maior = n3
if n1 < n2:
    menor = n1
else:
    menor = n2
if n3 < menor:
    menor = n3

print(maior)
print(menor)