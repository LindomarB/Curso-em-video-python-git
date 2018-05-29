##Exercício Python 015:Exercício Python 015:
# Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
c = float(input('quantos dias o carro foi alugado?: '))
c = (c*60.00)
km = float(input('quantos km foram percorridos ?: '))
km = (km*0.15)
print('o valor do carro foi {}\n e da kilometragem foi {}\n o valor total a pagar é {}'.format(c, km, km+c))

