# escreva um program que leia dois numeros inteiro
#e compare os mostrando na tela uma mensagem
# o primeiro valor e maior
#o segundo valor e maior
# nao existe valor maior os dois sao iguais
n1 = int(input('digiter um numero: '))
n2 = int(input('digite outro numero: '))
if n1 > n2:
    print('o maio valor é ', n1)
elif n2 > n1:
    print('o maior valor é ', n2)
else:
    print('os valores sao iguais')
