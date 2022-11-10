# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador
# vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar
# adivinhar até acertar, mostrando no final quantos palpites foram necessários
# para vencer.

import random
erros = 0
aleatorio = random.randint(0, 10) #gera um numero aleatorio de 0 a 10
#print(aleatorio)
numero = int(input('digite um numero para comparar com o gerador de 0 a 10: '))
while numero != aleatorio:
    erros += 1
    if numero > aleatorio:
        numero = int(input('um pouco menos: '))
    if numero < aleatorio:
        numero = int(input('um pouco mais: '))
print('voce acertou! o numero era {}! para isso têve que errar {} vezes O_O'.format(aleatorio, erros))
