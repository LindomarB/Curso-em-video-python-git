##Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa
#o programa vai perguntar o valor da cas #
#o salario do comprador#
#e quantos anos ele vai pagar#
#Calcule o valor da prestaçao mensal#
#sabendo que ela nao pode exceder 30% do salaio #
#u entao o emprestimo sera negado##
casa = float(input('digite o valor da casa:'))
salario = float(input('digite o salario: '))
ano = int(input('quantos anos deseja pagar o emprestimo?:'))
mensal = casa / (ano * 12)
print('{:.2f}'.format(mensal))
if mensal > (salario*30)/100:
    print('operaçao negada')
else:
    print('emprestimo liberado')