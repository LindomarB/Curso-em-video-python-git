# Desenvolva um programa que leia seis números inteiros e
#  mostre a soma apenas daqueles que forem pares.
#  Se o valor digitado for ímpar, desconsidere-o.#
soma = cont = 0
for c in range(1, 7):
    num = int(input('digite o {} valor: '.format(c)))
    if num %2 ==0:
        soma += num
        cont += 1
print('voce digitou {} valores pares \n e a soma dos pares é {}'. format(cont, soma))
