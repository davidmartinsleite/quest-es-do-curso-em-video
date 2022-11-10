# Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo
# e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.

inicio = int(input('digite o primeiro termo de uma razão: '))
razao = int(input('digite o valor da razão: '))
contador = 1
while contador <= 10:
    print('{} '.format(inicio), end='> ')
    inicio += razao
    contador += 1
print('FIM')
