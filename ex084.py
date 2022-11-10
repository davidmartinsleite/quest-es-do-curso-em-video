# Exercício Python 084: Faça um programa que leia nome e peso de
# várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = list()
dados = list()
pesadas = []
leves = []
continuar = 'S'
while continuar == 'S':
    dados.append(str(input('nome: ')))
    dados.append(int(input('peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    while True:
        continuar = input('deseja continuar[S/N/? ').strip().upper()[0]
        if continuar in 'SN':
            break
        else:
            print('valor invalido...')
pesada = leve = pessoas[0][1]
print(f'{len(pessoas)} foram cadastradas')
for p in pessoas:
    if p[1] >= 100:
        pesadas.append(p[:])
        if p[1] >= pesada:
            pesada = p[1]
    else:
        leves.append(p[:])
        if p[1] <= leve:
            leve = p[1]
print(f'o maior peso foi: {pesada}, as pessoas pesadas: ', end='')
for p in pesadas:
    print(f' {p[0]} ', end='')
print(f'\no menor peso foi: {leve}, as pessoas leves: ', end='')
for p in leves:
    print(f' {p[0]} ', end='')
