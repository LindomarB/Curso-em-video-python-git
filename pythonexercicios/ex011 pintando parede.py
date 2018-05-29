# faça um programa que leia a largura e a altura de uma
# parede e mostre sua area e a quantidade de tinta para pinta-la
# sabendo que cada litro de tinta pinta 2 m*2


a = float(input('digite a altura da parede: '))
b = float(input('digite a largura da parede: '))
area = a * b
print('sua parede tem {} metros quadrados. e prescisará de {:.2f} litros de tinta para ser pintada'.format(area, area/2))

