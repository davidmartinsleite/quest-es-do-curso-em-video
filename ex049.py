# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um
# que o usuário escolher, só que agora utilizando um laço for.

base = int(input('digite o valor base da tabuada: '))
for c in range(1, 11):
    print('{} X {} = {}'.format(c, base, c  * base))
