# Exercício Python 100: Faça um programa que tenha uma lista chamada
# números e duas funções chamadas sorteia() e somaPar(). A primeira
# função vai sortear 5 números e vai colocá-los dentro da lista e a
# segunda função vai mostrar a soma entre todos os valores pares
# sorteados pela função anterior.

import random
numeros = []


def aleatorio(dados):
    for r in range(5):
        aleatorio = random.randint(0, 9)
        numeros.append(aleatorio)
    print(f'sorteando {r+1} valores da lisa: {dados}')


def soma_par(dados):
    soma = 0
    for par in dados:
        if par % 2 == 0:
            soma += par
    print(soma)


aleatorio(numeros)
soma_par(numeros)
