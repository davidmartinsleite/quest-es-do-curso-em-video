# Exercício Python 50: Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares. Se o valor digitado for
# ímpar, desconsidere-o.
soma = 0
for c in range(1 ,7):
    n = int(input('digite o {}º numero: '.format(c)))
    if n % 2 == 0:
        soma += n
print('a soma dos numeros inteiros é {}'.format(soma))

