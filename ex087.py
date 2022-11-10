# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = soma3 = primeiro = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'digite o valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]
        if c == 2:
            soma3 += matriz[l][c]
        if l == 1:
            if primeiro == 0:
                maior = matriz[l][c]
            if matriz[l][c] > maior:
                maior = matriz[l][c]
    print()
print(f'a soma de todos os valores pares digitados é : {somap}')
print(f'A soma dos valores da terceira coluna é: {soma3}')
print(f'O maior valor da segunda linha é: {maior}')
