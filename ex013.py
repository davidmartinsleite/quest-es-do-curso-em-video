salario = float(input('digite o salario do funcionario: '))
aumento = float(input('digite a quamtidade em % que seu funcionario vai recener: '))
aumento = salario * (aumento / 100)
print('o salario de {} teve um almento de {} ficando {} reais, parabens pelo almento!'.format(salario, aumento, salario + aumento))
