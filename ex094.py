# Exercício Python 094: Crie um programa que leia nome, sexo e
# idade de várias pessoas, guardando os dados de cada pessoa em
# um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoas = []
informacoes = {}

while True:
    informacoes['nome'] = input('nome: ')
    while True:
        sexo = input('sexo: [M/f] ').strip().upper()
        if sexo in 'MF':
            informacoes['sexo'] = sexo
            break
        else:
            print('dados invalidos...')
    informacoes['idade'] = int(input('idade: '))
    pessoas.append(informacoes.copy())
    while True:
        continuar = input('continua? [S/N] ').strip().upper()
        if continuar in 'SN':
            break
        else:
            print('dados invalidos...')
    if continuar == 'N':
        break
print(pessoas)

soma_idades = 0
print(f'um total de {len(pessoas)} pessoas foram cadastradas')

for pessoa in pessoas:
    soma_idades += pessoa['idade']
media_idade = soma_idades / len(pessoas)

print(f'a media de idade é {media_idade:.1f}')

mulheres = []
for pessoa in pessoas:
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa)
print(f'as mulheres são: {mulheres}')

pessoas_acima_da_media = []
for pessoa in pessoas:
    if pessoa['idade'] > media_idade:
        pessoas_acima_da_media.append(pessoa)
print(f'a pessoas acima da media são: {pessoas_acima_da_media}')





