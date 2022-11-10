# Exercício Python 070: Crie um programa que leia o nome e o
# preço de vários produtos. O programa deverá perguntar se o
# usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
gastos = primeiro = caro = barato = 0
while True:
    produto = input('informe o nome do produto: ')
    preco = int(input('informe o valor do produto: '))
    primeiro += 1
    if primeiro == 1:
        barato = preco
    if preco < barato:
        barato = preco
        produto_barato = produto
    if preco >= 1000:
        caro += 1



    gastos += preco
    while True:
        continuar = input('deseja continuar?[S/N]: ').strip().upper()[0]
        if continuar in 'SN':
            break
        print('valor digitado invalido...')
    if continuar == 'N':
        break
print(f'o valor total gasto foi de {gastos} reais!')
print(f'um total de {caro} produtos foram comprados custando mais de 1000 reais')
print(f'o produto mais barato foi {produto_barato} custando {barato} reais')
