salario = float(input('digite o valor do seu salario: '))
if salario > 1250:
    print('seu salario passa a ser {:.2f} reais, parabens!'.format(salario * 1.1))
else:
    print('seu salario passa a ser {:.2f} reais, parabens!'.format(salario * 1.15))
