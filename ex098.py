# Exercício Python 098: Faça um programa que tenha uma função chamada
# contador(), que receba três parâmetros: início, fim e passo. Seu programa
# tem que realizar três contagens através da função criada:
#
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
import time


def contador(inicio, fim, passo):
    if fim > inicio:
        final = 1
    elif fim < inicio:
        final = -1
    for n in range(inicio, fim+final, passo):
        print(n)
        time.sleep(0.3)
    print()


contador(1, 10, 1)
contador(10, 0, -1)
contador(
    int(input('inicio: ')),
    int(input('fim: ')),
    int(input('passo: '))
)
