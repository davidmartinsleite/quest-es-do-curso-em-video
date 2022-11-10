# Exercício Python 069: Crie um programa que leia a idade e o
# sexo de várias pessoas. A cada pessoa cadastrada, o programa
# deverá perguntar se o usuário quer ou não continuar. No final,
# mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

maior18 = homens = mulheres20 = 0
while True:
    while True:
        sexo = input('informe o sexo do individuo[M/F]: ').strip().upper()[0]
        if sexo in 'MF':
            break
        print('valor digitado invalido...')
    idade = int(input('digite a idade: '))
    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        homens += 1
    if idade <= 20 and sexo == 'F':
        mulheres20 += 1
    while True:
        continuar = input('deseja continuar?[S/N]: ').strip().upper()[0]
        if continuar in 'SN':
            break
        print('valor digitado invalido...')
    if continuar == 'N':
        break
print(f'existem {maior18} pessoas maiores de 18 anos')
print(f'existem {homens} homens no grupo')
print(f'existem {mulheres20} mulheres com menos de 20 anos')