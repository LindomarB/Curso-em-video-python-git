##Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
# ## o primeiro e o último nome separadamente.


n = str(input('digite seu nome:')).upper().strip()
nome = n.split()
print('seu primeiro nome é {}'.format(nome[0]))
print('seu ultimo nome é {}'.format(nome[len(nome)-1])) ## comprimento de (len) de nom - 1 para indicar a ultima posiçao da lista

