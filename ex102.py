# Exercício Python 102: Crie um programa que tenha uma função
# fatorial() que receba dois parâmetros: o primeiro que indique
# o número a calcular e outro chamado show, que será um valor lógico
# (opcional) indicando se será mostrado ou não na tela o processo de
# cálculo do fatorial.

def fatorial(num=1, mostrar=False):
    '''
    calcula o fotorial de um numero, tambem pode mostrar o calculo na tela
    :param num: o valor do fatorial
    :param mostrar: caso joga para True mostra o calculo
    :return: o valor total da fatorial
    '''
    f = 1
    for c in range(num, 0, -1):
        if c == 1:
            print(' 1 ', end='')
        elif mostrar:
            print(f' {c} X', end='')
        f *= c
    if mostrar:
        print(f'= {f}')
    return f


n = int(input('digite um número: '))
mostrar = bool(input('digite qualquer tecla para mostrar o calculo: '))
print(f'o fatorial de {n} é igual a {fatorial(n, mostrar)}')
duvida = input('duvida com o programa? (S/N): ').strip().upper()
if duvida == 'S':
    help(fatorial)

