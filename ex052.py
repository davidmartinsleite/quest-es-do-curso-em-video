# Exercício Python 52: Faça um programa que leia um número inteiro e
# diga se ele é ou não um número primo.
divisivel = 0
numero = int(input('digite um numero: '))
for c in range(1, numero+1):
    if numero % c == 0:
        print('\033[31m{}\033[m'.format(c), end=' ')
        divisivel += 1
    else:
        print('\033[32m{}\033[m'.format(c), end=' ')
print(' \n ')
if divisivel == 2:
    print('o numero {} é um numero primo!'.format(numero))
else:
    print('o numero {} \033[31mNÃO\033[m é um numero primo!'.format(numero))
