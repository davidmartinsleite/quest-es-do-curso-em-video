# Exercício Python 081: Crie um programa que vai ler vários
# números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

valores = list()
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
print(f'foram digitados {len(valores)} valores')
valores.sort(reverse=True)
print(f'a lista em ordem decrecente é: {valores}')
if 5 in valores:
    print(f'o numero 5 está presente na {valores.index(5)}° celula')
else:
    print('o valor 5 não está presente na lista')
