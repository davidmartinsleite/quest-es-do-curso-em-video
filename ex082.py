# Exercício Python 082: Crie um programa que vai ler vários
# números e colocar em uma lista. Depois disso, crie duas listas
# extras que vão conter apenas os valores pares e os valores
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo
# das três listas geradas.

valores = list()
valoresI = []
valoresP = []
continuar = 'S'
while continuar == 'S':
    dado = int(input('digite um valor para a lista: '))
    valores.append(dado)

    while True:
        continuar = input('deseja continuar[S/N/? ').strip().upper()[0]
        if continuar in 'SN':
            break
        else:
            print('valor invalido...')
for c in valores:
    if c % 2 == 0:
        valoresP.append(c)
    else:
        valoresI.append(c)
print(f'a lista com todos os valores: {valores}')
print(f'com os valores impares: {valoresI}')
print(f'com os valores pares: {valoresP}')
