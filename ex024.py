# Exercício Python 24: Crie um programa que leia o nome de uma
# cidade diga se ela começa ou não com o nome “SANTO”.

cidade = input('digite o nome da sua cidade: ')
cidade = cidade.split()
cidade = cidade[0].upper()
print(cidade == 'SANTO')

