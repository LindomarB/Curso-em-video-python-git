#programa que valida dados#
sexo = str(input('qual o seu sexo [M/F]: ')).strip()
while sexo not in 'm M F f ':
    print('operaçao inválida')
    sexo = str(input('qual o seu sexo [M/F]: ')).strip()
print('Operaçao validada')