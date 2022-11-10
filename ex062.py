# Exercício Python 062: Melhore o DESAFIO 061, perguntando para o
# usuário se ele quer mostrar mais alguns termos. O programa encerrará
# quando ele disser que quer mostrar 0 termos.

inicio = int(input('digite o primeiro termo de uma razão: '))
razao = int(input('digite o valor da razão: '))
contador = 1
novamente = 10
repete = 1
while repete != 0:
    while contador <= novamente:
        print('{} '.format(inicio), end='> ')
        inicio += razao
        contador += 1
    repete = int(input('quantos termos você quer mostrar a mais? '))
    novamente += repete
print('FIM')
