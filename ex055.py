# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
maior_peso = 0
menor_peso = 999

for c in range(1, 6):
    peso = float(input('digite o peso da {}° pessoa: '.format(c)))
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso
print('o maior peso registrado foi de {}kg\n'
      'o menor peso registrado foi de {}kg'.format(maior_peso, menor_peso))
