# Exercício Python 075: Desenvolva um programa que leia quatro
# valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite o segundo numero: '))
n3 = int(input('digite o terceiro numero: '))
n4 = int(input('digite o quarto numero: '))
tupla = (n1, n2, n3, n4)
print(f'esses são os numeros celecionados: {tupla}')
print(f'o numero 9 pareceu {tupla.count(9)} vezes')
if 3 in tupla: #ele  procura o valor 3 dentro de tupla
    print(f'o numero 3 aparece primeiro na {tupla.index(3)+1}° celula')
else:
    print('o valor 3 não aparece no sistema')
print('os numeros pares são: ', end='')
for c in range(0, 4):
    if tupla[c] % 2 == 0:
        print(tupla[c], end=' ')
