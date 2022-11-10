# Exercício Python 088: Faça um programa que ajude um jogador
# da MEGA SENA a criar palpites.O programa vai perguntar quantos
# jogos serão gerados e vai sortear 6 números entre 1 e 60 para
# cada jogo, cadastrando tudo em uma lista composta.
import time
import random
acumulador = 0
palpites =[]
seguencia = []
apostas = int(input('digite a quantidade de palpites que você quer gerar: '))
for p in range(0, apostas):
    while True:
        aleatorio = random.randint(1, 60)
        if aleatorio not in seguencia:
            seguencia.append(aleatorio)
            acumulador += 1
            if acumulador == 6:
                break
    seguencia.sort()
    print(seguencia)
    palpites.append(seguencia[:])
    seguencia.clear()
    acumulador = 0
    time.sleep(1)

