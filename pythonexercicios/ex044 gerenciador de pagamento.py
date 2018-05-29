##elabore um programa que calcule o valor a ser pago
#por um produto considerando o seu preço normal e condiçao de pagamento
#a vis dinheiro ou chequue 10% de deconto
#a vista no cartao 5%
#em ate 2x no cartao preço normal
#3x ou mais no cartao 20% de juros  ##
n = float(input('qual o valor do produto: '))
avd = n - (n * 10)/100
avc = n - (n * 5)/100
car2x = n
car3x = (n * 20)/100 + n
p = int(input('''forma de pagamento:
1 dinheiro 10% de desconto
2 a vista no cartao 5% de descont
3 em ate 2x no cartao sem desconto e sem jusos
4 3x no cartao + 20% de juros: \n'''))
if p == 1:
    print(avd)
elif p == 2:
    print(avc)
elif p == 3:
    print(car2x)
elif p == 4:
    print(car3x)
else:
    print('operaçao invalida')