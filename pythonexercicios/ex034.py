#escreva um programa que pergunte o salario do funcionario
#e calcule seu aumento
#para salarios superiores a 1250.00 calcule aumento de 10%
#para inferiores ou iguais o aumento e de 15%

sal = float(input('digite o valor do salario do funcionario \n'))
if sal <= 1250:
    print('o novo salario do funcionario sera {:.2f} reais.'.format((sal*15)/100 + sal))
else:
    print('o novo salario do funcionario sera de {:.2f} reais.'.format((sal*10)/100 + sal))
