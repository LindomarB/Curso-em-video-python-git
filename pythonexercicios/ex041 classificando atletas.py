# crie um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria de acordo com a idade
# ate 9 anos mirim
# ate 14 infantil
# ate 19 junior
# ate 20 senior
# acima: master##
idade = int(input('digite a idade do atleta:'))
if idade <= 9:
    print('mirim sua idade é {}'.format(idade))
elif idade <=14:
    print('infantil sua idade é {}'.format(idade))
elif idade <= 19:
    print('junior sua idade é {}'.format(idade))
elif idade <= 20:
    print('senior sua idade é {}'.format(idade))
elif idade <= 25:
    print('master sua idade é {}'.format(idade))
else:
    print('sua classificaçao e master')
