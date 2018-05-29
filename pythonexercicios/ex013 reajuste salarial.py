# faça um programa que leia o salario de um funcionario.
# e mostre o seu salario e o novo salario com mais 15 % de aumento


salario = float(input('digite o valor do salario do funcionario: '))
nsal = (salario*15/100)
print('o reajuste de 15% sera de {:.2f}. \n e o salario total do funcionario será {:.2f}'.format(nsal, salario + nsal))
