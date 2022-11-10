# Exercício Python 068: Faça um programa que jogue par ou ímpar
# com o computador. O jogo só será interrompido quando o jogador
# perder, mostrando o total de vitórias consecutivas que ele
# conquistou no final do jogo.

import random
acertou = 0
print('joguinho de par ou impart')
while True:
    aleatorio = random.randint(0, 1)
    while True:
        jogador = input('digite impart [i] ou par [p]: ').strip().upper()[0]
        if jogador in 'IP':
            break
        print('valor invalido por favor preencha com "i" ou "p"')
    if jogador == 'I':
        valor = 0
    elif jogador == 'P':
        valor = 1

    if aleatorio == valor:
        print('parabens você acertou!')
        acertou += 1
    else:
        break
print(f'você acertou {acertou} vezes')
