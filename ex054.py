# Exercício Python 54: Crie um programa que leia o ano de nascimento de
# sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantas já são maiores.

import datetime

maior_idade = 0
menor_idade = 0
ano_atual = datetime.datetime.today().year
for pessoa in range(1, 7):
    ano = int(input('digite o ano de nascimento da {}° pessoa: '.format(pessoa)))
    if ano_atual - ano > 18:
        maior_idade += 1
    else:
        menor_idade += 1
print('existem {} pessoas maiores de idade \n'
      'existem {} pessoas menores de idade'.format(maior_idade, menor_idade))
