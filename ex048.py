# Exercício Python 48: Faça um programa que calcule a soma entre todos
# os números que são múltiplos de três e que se encontram no intervalo
# de 1 até 500.
soma = 0
for c in range(1, 500+1, 2):
    resto = c % 3
    if resto == 0:
        print(c)
        soma += c
print(soma)
