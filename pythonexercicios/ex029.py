##escreva um program que leia a velocidade de um carro
## se ele ultrapassar 80 km/h mostre uma msg dizendo que ele foi multado
##a multa vai custar 7 pila por cada km acima do limite

velo = float(input('qual a velocidade do veiculo ?: '))
if velo >= 81.0:
    print('voce esta a {} km/h acima do limite \n e pagara {} Reais de multa seu bosta'.format(velo - 80, (velo - 80)*7))