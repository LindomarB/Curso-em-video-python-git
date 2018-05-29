## calcular media aritmetica
## mostrar as duas notas do aluno. e calcular a media.

nome = input('digite seu nome: ')
n1 = float(input('digite a primeira nota do aluno: '))
n2 = float(input('digite a segunda nota do aluno: '))
s = (n1 + n2)/2
print('a media do aluno {} é {:.1f}'.format(nome, s))

