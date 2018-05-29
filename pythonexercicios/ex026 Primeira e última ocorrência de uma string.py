##Faça um programa que leia uma frase pelo teclado e mostre
# ##quantas vezes aparece a letra "A", em que posição ela
# #aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('digite algo:')).upper().strip()
print('a letra a aparece {} vezes'.format(frase.count('A')))
print('a letra A aparece primeiro na posicao {}'.format(frase.find('A')+1))
print('a ultima letra na posiçao {}'.format(frase.rfind('A')+1))### rfind começa a procura primeiro pelo final

