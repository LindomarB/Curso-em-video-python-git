#Faça um programa que calcule a soma entre todos os números que são
# múltiplos de três e que se encontram no intervalo de 1 até 500.#
soma = cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c, end=' ')
        soma += c
        cont += 1
print('a soma de todos os cvalores é {} foram {} numeros'.format(soma, cont))