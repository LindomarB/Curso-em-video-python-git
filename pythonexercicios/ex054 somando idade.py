from datetime import date
totmaior = totmenor = 0
atual = date.today().year
for c in range(1, 6):
    nasc = int(input('em que ano a pessoa nasceu: '))
    idade = atual - nasc
    print(idade)
    if idade >= 21:
        totmaior += 1
        print('ja é maior de idade')
    else:
        totmenor += 1
        print('é menor de idade')
print('ha {} pessoas maiores de idade'.format(totmaior))
if totmenor >= 1:
    print(' e {} pessoas menores de idade'.format(totmenor))
else:
    print('nao ha pessoas menores de idade no grupo de pessoas digitadas')