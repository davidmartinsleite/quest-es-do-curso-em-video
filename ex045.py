# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

import random
import time
computador = random.randint(1, 3)
jogador = int(input('''[ 1 ] pedra
[ 2 ] papel
[ 3 ] tesoura
digite sua opão: '''))
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔ!!!')
if jogador == 1 and computador == 2:
    print('papel ganha de tesoura, o computador ganhou')
elif jogador == 2 and computador == 3:
    print('tesoura ganha de papel, o computador ganhou')
elif jogador == 3 and computador == 1:
    print('pedra ganha de tesoura, o computador ganhou')

elif jogador == 2 and computador == 1:
    print('papel ganha de tesoura, você ganhou!')
elif jogador == 3 and computador == 2:
    print('tesoura ganha de papel, você ganhou!')
elif jogador == 1 and computador == 3:
    print('pedra ganha de tesoura, você ganhou!')


