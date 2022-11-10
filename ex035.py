n1 = int(input('escreva a primeira reta do triangulo: '))
n2 = int(input('escreva a segunda reta do triangulo: '))
n3 = int(input('escreva a terceira reta do triangulo: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('ele pode formar um triangulo!')
else:
    print('esses valores não podem formar um triangulo')
