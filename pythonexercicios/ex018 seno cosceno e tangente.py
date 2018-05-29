# faça um programa que leia um angulo qualquer
#  e mostre na tela o valor do
# #seno cosseno e tangente desse angulo
import math
a = float(input('digite o angulo que voce deseja:'))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tg = math.tan(math.radians(a))
print('o angulo de {} tem seno de {:.2f}'.format(a, sen))
print('o angulo de {} tem cosseno de {:.2f}'.format(a, cos))
print('o angulo de {} tem tangente de {:.2f}'.format(a, tg))
print('pronto desgraça!!!!!')
