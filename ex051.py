# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e
# a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

inicio = int(input('digite o primeiro termo de uma razão: '))
razao = int(input('digite o valor da razão: '))
for c in range(inicio, inicio+10):
    inicio += razao
    print('{} '.format(inicio), end = '> ')
print('FIM')
