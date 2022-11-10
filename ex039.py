# Exercício Python 39: Faça um programa que leia o ano de nascimento de um
# jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar
# ao serviço militar, se é a hora exata de se alistar ou se já passou do
# tempo do alistamento. Seu programa também deverá mostrar o tempo que falta
# ou que passou do prazo.

import datetime

ano = int(input('digite seu ano de nascimento: '))
data = datetime.datetime.today().year
idade = data - ano
if idade < 18:
    print('falta {} anos para o alistamento'.format(-1*(idade - 18)))
elif idade == 18:
    print('esse ano é de alistamento!')
else:
    print('você passou {} anos sem se alistar'.format(idade - 18))
