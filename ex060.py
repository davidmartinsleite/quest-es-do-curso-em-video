# Exercício Python 060: Faça um programa que leia um número qualquer e mostre
# o seu fatorial.
#
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

numero = int(input('digite um numero para fazer a fatorial do mesmo: '))
print('{}! = {} '.format(numero, numero), end='')
fatorial = numero
while numero != 1:
    numero -= 1
    fatorial = fatorial * numero
    print('x {} '.format(numero), end='')
print(' = {}'.format(fatorial))
