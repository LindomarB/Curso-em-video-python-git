from random import randint
acertou = False
palpite = 0
comp = randint(0, 10)
print(comp)
while not acertou:
    j1 = int(input('qual o seu palpite: '))
    if j1 == comp:
        acertou = True
        palpite += 1
    else:
        if j1 < comp:
            print('mais')
            palpite += 1
        if j1 > comp:
            print('menos')
            palpite += 1
print(' Voce Acertou com {} tentativas.'. format(palpite))