#um professor quer sortear
# entre seus quatro alunos.
#faça um programa que leia o nome deles e mostre na tela o nome sorteado
import random
a = str(input('digite o nome do aluno: '))
b = str(input('digite o nome do aluno: '))
c = str(input('digite o nome do aluno: '))
d = str(input('digite o nome do aluno: '))
lista = [a, b, c, d]
escolha = random.choice(lista)
print('o escolhido foi {}'. format(escolha))
