# Exercício Python 063: Escreva um programa que leia um número N
# inteiro qualquer e mostre na tela os N primeiros elementos de uma
# Sequência de Fibonacci.

# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

tamanho = (int(input('defina o tamanho da fibonacci: '))) - 3
contador = 0
t1 = 0
t2 = 1
print('{} - {} '.format(t1, t2), end='')
while contador <= tamanho:
    t3 = t1 + t2
    print('- {} '.format(t3), end='')
    t1 = t2
    t2 = t3
    contador += 1
