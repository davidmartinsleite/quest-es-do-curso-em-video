# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que
# leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#
# – Até 9 anos: MIRIM
#
# – Até 14 anos: INFANTIL
#
# – Até 19 anos: JÚNIOR
#
# – Até 25 anos: SÊNIOR
#
# – Acima de 25 anos: MASTER

import datetime

nascimento = int(input('digite o seu ano de nascimento para indentificar qual categoria você pertence: '))
data = datetime.date.today().year
idade = data - nascimento
if idade <= 9:
    print('o atleta de {} anos pertence a categoria mirim'.format(idade))
elif 9 < idade <= 14:
    print('o atleta de {} anos pertence a categoria infantil'.format(idade))
elif 14 < idade <= 19:
    print('o atleta de {} anos pertence a categoria júnior'.format(idade))
elif 19 < idade <= 25:
    print('o atleta de {} anos pertence a categoria sênior'.format(idade))
elif 26 < idade:
    print('o atleta de {} anos pertence a categoria master'.format(idade))
else:
    print('valor invalido')
