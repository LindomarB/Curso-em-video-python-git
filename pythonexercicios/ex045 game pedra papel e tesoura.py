##faça um jogo pedra papel e tesoura
#1 pedra 2 tesouea 3 papel
#o computador jogara com vc
##modulo random de uma lista? ##
import random
pd = 1
p = 2
t = 3
j2 = random.choice([1, 2, 3])

j1 = int(input('''1 pedra
2 papel
3 tesoura:\n '''))
print('voce escolheu {} e adversario escolheu {}'.format(j1, j2))
if j1 == j2:
  print('empate')
elif j1 == 1 and j2 == 2:
  print('voce perdeu pedra perde de papel')
elif j1 == 2 and j2 == 3:
  print('voce perdeu papel perde para tesoura')
elif j1 == 3 and j2 == 1:
  print("voce perdeu tesoura perde de pedra")
elif j2 == 1 and j1 == 2:
  print('voce ganhou pedra perde de papel')
elif j2 == 2 and j1 == 3:
  print('voce ganhou papel perde para tesoura')
elif j2 == 3 and j1 == 1:
  print("voce ganhou tesoura perde de pedra")
elif j1 > 4:
  print('jogada invalida')
else:
  print('comando invalido')


