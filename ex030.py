numero = int(input('escreva um numero: '))
resto = numero % 2 #a "%" representa o MÓDULO da divisão
if resto == 0:
    print('o numero {} é par'.format(numero))
else:
    print('o numero {} é impar'.format(numero))
