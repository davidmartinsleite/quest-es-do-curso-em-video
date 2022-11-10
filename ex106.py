# Exercício Python 106: Faça um mini-sistema que utilize o
# Interactive Help do Python. O usuário vai digitar o comando e o
# manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o
# programa se encerrará. Importante: use cores.


def escreva_verde(texto):
    tamanho = len(texto) + 4
    print('\033[1;39;42m~'*tamanho)
    print(f'  {texto}')
    print('~'*tamanho)
    print('\033[m')


def escreva_azul(texto):
    tamanho = len(texto) + 4
    print('\033[1;39;44m~'*tamanho)
    print(f'  {texto}')
    print('~'*tamanho)
    print('\033[m')


def escreva_branco(texto):
    tamanho = len(texto) + 4
    print('\033[7;30;38m~' * tamanho)
    print(f'  {texto}')
    print('~' * tamanho)
    print('\033[m')

def ajuda():
    import time
    escreva_verde('sistema de ajuda pyHELP')
    while True:
        funcao = input('função ou biblioteca: ')
        escreva_azul(f'acessando o comando {funcao}')
        time.sleep(1)
        print('\033[7;30;38m~', end='')
        help(funcao)
        print('\033[m')
        if funcao == 'fim':
            break
    print('FIM DO PROGRAMA')

ajuda()
#escreva_branco('teste')
