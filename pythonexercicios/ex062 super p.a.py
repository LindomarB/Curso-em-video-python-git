#Melhore o DESAFIO 061, perguntando para o usuário se ele
# quer mostrar mais alguns termos. O programa
# encerrará quando ele disser que quer mostrar 0 termos#
primeiro = int(input('digite o primeiro termo: '))
razao = int(input('digite a razao: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ->'.format(termo), end='')
        termo += razao
        cont += 1
    print('pausa')
    mais = int(input('quantos trmos vc deseja mostrar a mais: [0] para sair'))
print('FIM')
print('voce digitou ao total {} termos'.format(total))