# Exercício Python 065: Crie um programa que leia vários números inteiros
# pelo teclado. No final da execução, mostre a média entre todos os valores
# e qual foi o maior e o menor valores lidos. O programa deve perguntar ao
# usuário se ele quer ou não continuar a digitar valores.

soma = contador = menor = maior = 0

continuar = 'S'
while continuar == 'S':
    numero = int(input('digite um número: '))
    soma += numero
    contador += 1
    if contador == 1:
        menor = numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    continuar = input('quer continuar? [S/N] ').strip().upper()[0]
    while continuar not in 'SN':
        print('valor incorreto repita a operação...')
        continuar = input('quer continuar? [S/N] ').strip().upper()[0]
print('você digitou {} números e a média foi de {}'.format(contador, soma / contador))
print('o maior valor foi {} e o menor foi {}'.format(maior, menor))
