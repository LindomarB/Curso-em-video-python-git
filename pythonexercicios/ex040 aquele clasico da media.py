# calcular a media
#media abaixo de 5,0 reprovado
#media entre 5 e 6,9 recuperaçao
# media 7,0 ou > aprovado
n1 = float(input('digite a primeira nota do aluno cabeça de bagre:'))
n2 = float(input('digite a segunda nota do aluno abestado: '))
m = (n1 + n2)/2
if m >= 7.0:
    print('aluno ze ruela aprovado com {} de media '.format(m))
elif m >= 5 and m <= 6.9:
    print('aluno burro da porra vai pra recuperaçao!!! nota {}'.format(m))
elif m < 5.0:
    print(' aluno idiota e escroto nao estudou o ano inteiro agora chora pra professor por nota pqp nota {}'.format(m))

print(m)