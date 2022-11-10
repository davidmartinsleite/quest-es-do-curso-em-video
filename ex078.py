# Exercício Python 078: Faça um programa que leia 5 valores
# numéricos e guarde-os em uma lista. No final, mostre qual
# foi o maior e o menor valor digitado e as suas respectivas
# posições na lista.

valores = list()
for c in range(0, 5):
   valores.append(int(input(f'digite a valor da {c}° celula: ')))
print(f'você digitou os valores: {valores}')
print(f'o valor maximo digitado foi {max(valores)}, na posição: ', end='')
for c, v in enumerate(valores):
    if v == max(valores):
        print(f' {c} ', end='')
print(f'\no valor minimo digitado foi {min(valores)}, na posição: ', end='')
for c, v in enumerate(valores):
    if v == min(valores):
        print(f' {c} ', end='')
