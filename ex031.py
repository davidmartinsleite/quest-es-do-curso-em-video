distancia = float(input('digite a distancia em quilometros da viagem: '))
if distancia < 200:
    print('a passagem vai custar {:.2f} reais'.format(distancia * 0.5))
else:
    print('a passagem vai custar {:.2f} reais'.format(distancia * 0.45))
