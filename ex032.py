ano = int(input('escreva um ano para saber se é bisiesto: '))
resto = ano % 4 #a "%" representa o MÓDULO da divisão
if resto == 0:
    print('o ano {} é bisiesto'.format(ano))
else:
    print('o ano {} não é bisiesto'.format(ano))
