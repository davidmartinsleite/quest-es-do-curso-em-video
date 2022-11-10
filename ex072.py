# Exercício Python 072: Crie um programa que tenha uma Tupla
# totalmente preenchida com uma contagem por extenso, de zero
# até vinte. Seu programa deverá ler um número pelo teclado
# (entre 0 e 20) e mostrá-lo por extenso.

extenso = ('um', 'dois', 'três', 'quatro', 'sinco', 'seis', 'sete', 'oito', 'nove',
           'dez','onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezecete',
           'dezoito', 'dezenove', 'vinte')

while True:
    numero = int(input('digite um numero para ser mostrado em extenso: '))
    if 0 < numero <= 20:
        break
    print('numero invalido...')
print(f'numero {extenso[numero - 1]}')
