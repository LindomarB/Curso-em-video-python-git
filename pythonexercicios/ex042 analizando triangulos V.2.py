#refaça o desafio 035 dos triangulos
#acrescentando o recurso de mostrar que tipo
#de triangula sera formado:
# equilatero todos os lados iguais
# isosceles dois lados iguais
# escaleno todos os lados diferentes  ##
a = float(input('digite um numero: '))
b = float(input('digite outro numero: '))
c = float(input('digite um terceiro numero: '))

if a < b + c and b < a + c and c < a + b:
 print(' forma um triangulo ', end='')
 if a == b and b == c:
     print('equilatero')
 elif a != b and b != c and c != a:
     print('escaleno')
 else:
    print('escaleno')
else:
    print('nao formam um triangulo')