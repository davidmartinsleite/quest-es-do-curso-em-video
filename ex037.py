# Exercício Python 37: Escreva um programa em Python que leia um número
# inteiro qualquer e peça para o usuário escolher qual será a base de
# conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('insira um numero decimal, e escolha sua base de conversão: '))
base = int(input('escolha a base de conversão\n'
                 '1 - binario\n2 - octal\n3 - hexmal\n'))
if base == 1:
    print('o numero decimal de {} será {} binário'.format(numero, bin(numero)[2:]))
elif base == 2:
    print('o numero decimal de {} será {} octal'.format(numero, oct(numero)[2:]))
elif base == 3:
    print('o numero decimal de {} será {} hexadecimal'.format(numero, hex(numero)[2:]))
else:
    print('você digitou um valor invalido!')

