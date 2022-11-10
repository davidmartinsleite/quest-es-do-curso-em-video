# Exercício Python 099: Faça um programa que tenha uma função chamada
# maior(), que receba vários parâmetros com valores inteiros. Seu
# programa tem que analisar todos os valores e dizer qual deles é o maior.


import random


def maior(lista):
    print(lista)
    lista.sort()
    print(f'foram informados {len(lista)} ao todo')
    print(f'o maior numero foi {lista[-1]}')
    print()


dados = [2, 4, 2, 1, 9]
maior(dados)

for n in range(6, 1, -1):
    dados = []
    for r in range(n):
        aleatorio = random.randint(0, 9)
        dados.append(aleatorio)
    maior(dados)
