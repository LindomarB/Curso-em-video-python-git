#faça um programa que leia o nome dos quatro alunos
# #e mostre a ordem sorteada
import random
a = str(input('digite o nome do aluno: '))
b = str(input('digite o nome do aluno: '))
c = str(input('difite o nome do aluno: '))
d = str(input('digite o nome do aluno: '))
lista = [a, b , c, d]
escolhido = random.shuffle(lista)
print(lista)