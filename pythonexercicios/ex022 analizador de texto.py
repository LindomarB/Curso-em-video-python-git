##Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
##O nome com todas as letras maiúsculas e minúsculas.
##Quantas letras ao todo (sem considerar espaços).
##Quantas letras tem o primeiro nome.##


nome = input('digite seu nome completo:')
separa = nome.split()
print(nome)
nome = nome.upper()
print(nome)
nome = nome.lower()
print(nome)
print('se nome tem {} letras'. format(len(nome) - nome.count(' ')))
print('seu primeiro nome tem {} letras'.format(len(separa[0])))
print('seu nome invertido eh{} {}'.format(separa[1], separa[0]))





