####mostre se um numero digitado pelo usuario e par ou impar


##tentar usar modulo % resto da divisao
## % 2 ==0
## leia-se
## o modulo dividido por dois igual a zero
## ou seja o numero dividido por dois e o resto for zer osempre sera par caso contrario e impar


num = int(input('digite um numero: '))
if num % 2 == 0:
    print('e par')
else:
    print('e impar')
