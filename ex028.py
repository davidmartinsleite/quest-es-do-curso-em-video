import random

aleatorio = random.randint(0,5)#gera um numero aleatorio de 0 a 5
numero = int(input('digite um numero para comparar com o gerador de 0 a 5: '))
if 0 <= numero <= 5:
    if numero == aleatorio:
        print('parabens você acertou o numero!!!')
    else:
        print('você errou o numero geredo foi {}'.format(aleatorio))
else:
    print('o numero {} é invalido'.format(numero))
