# Exercício Python 074: Crie um programa que vai gerar cinco
# números aleatórios e colocar em uma tupla. Depois disso,
# mostre a listagem de números gerados e também indique o
# menor e o maior valor que estão na tupla.

import random
from random import randint #NOTA AQUI EU DEIXEI DE USAR A LIB GERAL
# PARA Q EU POSSA USAR APENAS A FUNÇÃO 'RANDINT' EVITANTO POLUIÇÃO NO CODIGO


numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))

numeros_ordenados = sorted(numeros)
print(f'os valores sorteados foram: {numeros}')
print(f'o maior numero é: {numeros_ordenados[-1]}')
print(f'o menor numero é: {numeros_ordenados[0]}')

# OUTRO JEITO

print(f'o maior numero é: {max(numeros)}')
print(f'o menor numero é: {min(numeros)}')
