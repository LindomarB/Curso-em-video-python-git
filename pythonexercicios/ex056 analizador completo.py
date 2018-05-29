#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o
# nome do homem mais velho e quantas mulheres têm menos de 20 anos.#
soma = maior = cont =0
nomev = ''
for c in range(1, 5):
    print('=#'*20)
    nome = str(input('Digite o nome da {}ª pessoa: '.format(c)))
    sexo = str(input('qual e sexo da pessoa ?: ')).strip()[0].upper()
    if sexo == 'M':
        idade = int(input('qual a idade de {}: '.format(nome)))
    if sexo == 'F':
        idade = int(input('qual a idade da {}: '.format(nome)))
    soma += idade
    if 'M' in sexo and idade > maior:
        maior = idade
        nomev = nome
    if 'F' in sexo and idade < 21:
        cont += 1
print(' a media de idade do grupo é {}'.format(soma/4))
print(' O nome do homem mais velho no grupo é {}'.format(nomev))
if cont == 1:
    print(' há {} mulher no grupo com menos de 21 anos'.format(cont))
else:
    print(' há {} mulheres no grupo com menos de 21 anos'.format(cont))