# Exercício Python 092: Crie um programa que leia nome, ano
# de nascimento e carteira de trabalho e cadastre-o (com idade)
# em um dicionário. Se por acaso a CTPS for diferente de ZERO,
# o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa
# vai se aposentar.

import datetime
data = datetime.datetime.today().year
pessoa = {}
nome = str(input('digite seu nome: '))
nascimento = int(input('digite o ano de nascimento: '))
idade = data - nascimento
documento = int(input('carteira de trabalho (0 não tem): '))
if documento != 0:
    carteira = documento
    contratacao = int(input('ano de contratação: '))
    salario = int(input('salario: R$'))
    aposentadoria = (contratacao - data) + 35

print('-='*15)

pessoa['nome'] = nome
pessoa['idade'] = idade
if documento != 0:
    pessoa['carteira'] = carteira
    pessoa['contratacao'] = contratacao
    pessoa['salario'] = salario
    pessoa['aposentadoria'] = aposentadoria

print(f'nome: {pessoa["nome"]}')
print(f'idade: {pessoa["idade"]}')
if 'carteira' in pessoa:
    print(f'numero da carteira: {pessoa["carteira"]}')
    print(f'ano da contratação: {pessoa["contratacao"]}')
    print(f'salario: {pessoa["salario"]}')
    print(f'faltam {pessoa["aposentadoria"]} anos para a aposentadoria, isso vai ser em {pessoa["aposentadoria"] + data}')
