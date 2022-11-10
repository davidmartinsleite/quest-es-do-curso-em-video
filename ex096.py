# Exercício Python 096: Faça um programa que tenha uma função chamada área()
# , que receba as dimensões de um terreno retangular (largura e comprimento)
# e mostre a área do terreno.


def area_terreno():
    print('controle de terrenos')
    print('-'*20)
    l = int(input('lartgura(m): '))
    c = int(input('comprimento(m): '))
    a = l*c
    print(f'a área de um terreno {l}X{c} é de {a}m²')


area_terreno()