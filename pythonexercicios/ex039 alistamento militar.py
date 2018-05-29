##faça um programa que leia a idade de um jovem
#e informe de acordo com sua idade
#se ele ainda vai se alistar ao serviço militar
#se e a hora de se alistar
#se ja passou do tempo de se alistar
#o progrma tbm devera mostrar o tempo que falta ou que passou do prazo  ##
## faltam tantos ou ja se passaram tandos anos do alistamento
from datetime import date
atual = date.today().year
nasc = int(input('em que ano voce nasceu: '))
idade = atual - nasc
if idade == 18:
    print('hora de se alistar!')
elif idade < 17:
    print('voce ainda nao atingiu a idade para o alistamento. \nAinda faltam {} ano(s) para vc se alistar'.format(18-idade))
else:
    print('voce ja passou da idade de alistamento. \nJa se passaram {} ano(s) do seu alistamento'.format(idade-18))

print(atual)