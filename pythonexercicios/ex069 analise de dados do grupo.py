'''Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''
tot18 = toth = tot20 = 0
while True:
    idade = int(input('digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('qual o sexo [M/F]')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        tot20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('quer continuar ? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'São {tot18} pessoas com mais de 18 anos, {toth} são homens, e há {tot20} mulheres com menos de 20 anos')