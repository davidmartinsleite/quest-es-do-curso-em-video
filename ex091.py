# Exercício Python 091: Crie um programa onde 4 jogadores joguem
# um dado e tenham resultados aleatórios. Guarde esses resultados
# em um dicionário em Python. No final, coloque esse dicionário em
# ordem, sabendo que o vencedor tirou o maior número no dado.

import random
jogadores = {}
lugar = 1
for d in range(0, 4):
    aleatorio = random.randint(1, 6)
    jogadores[f'jogador{d}'] = aleatorio
for i in sorted(jogadores, key=jogadores.get, reverse=True): #cria uma ordem pelos valores
    print(f'{lugar}° lugar: {i} com {jogadores[i]}')
    #print(i, jogadores[i])
    lugar += 1
