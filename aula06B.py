#a função "is..." serve para indentificar que tipo de
# estrutura aquela valor está sendo representado

coisa = input('escreva qualquer coisa: ')
tipoDeCoisa = type(coisa)
print('isso é um {}'.format(tipoDeCoisa))
print('ele é um numerico? ', coisa.isnumeric())
print('ele é um numerico? ', coisa.isalnum())
print('ele é um alphanumerico? ', coisa.isalnum())
