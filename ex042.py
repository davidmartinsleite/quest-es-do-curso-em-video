# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso
# de mostrar que tipo de triângulo será formado:
#
# – EQUILÁTERO: todos os lados iguais
#
# – ISÓSCELES: dois lados iguais, um diferente
#
# – ESCALENO: todos os lados diferentes

n1 = int(input('escreva a primeira reta do triangulo: '))
n2 = int(input('escreva a segunda reta do triangulo: '))
n3 = int(input('escreva a terceira reta do triangulo: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('ele pode formar um triangulo!')
    if n1 == n2 == n3:
        print('esse triangulo é equilátero')
    elif n1 == n2 != n3:
        print('esse triangulo é isóceles')
    elif n1 == n3 != n2:
        print('esse triangulo é isóceles')
    elif n3 == n2 != n1:
        print('esse triangulo é isóceles')
    else:
        print('esse triangulo é escaleno')
else:
    print('esses valores não podem formar um triangulo')
