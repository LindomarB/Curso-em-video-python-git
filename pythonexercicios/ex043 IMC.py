# calcular o imc peso / alt. (float)
#e mostrar as seguintes informacoes
#abaico de 18,5 abaixo do peso
#entre 18,5 e 25 peso ideal
#25 ate 30 sobrepeso
#de 30 a 40 besidade
#acima de 40 obesidade morbida     ##
alt = float(input('Informe a sua Altura: '))
peso = float(input('Infome o seu Peso: '))

imc = peso / (alt * alt)

if imc < 18.5:
    print('O seu IMC e de {:.1f} voce esta abaixo do peso!'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('O seu IMC e de {:.1f} voce esta no seu peso ideal!'.format(imc))
elif imc > 25 and imc <= 30:
    print('O seu IMC e de {:.1f} voce esta com sobrepeso!'.format(imc))
elif imc > 30 and imc <= 40:
    print('O seu IMC e de {:.1f} voce esta com obesidade!'.format(imc))
elif imc > 40:
    print('O seu IMC e de {:.1f} voce esta com obesidade morbida!'.format(imc))