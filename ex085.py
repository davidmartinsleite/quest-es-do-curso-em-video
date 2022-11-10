# Exercício Python 085: Crie um programa onde o usuário possa
# digitar sete valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e ímpares. No final,
# mostre os valores pares e ímpares em ordem crescente.

valores = []
dados = []
par = []
impar = []
for c in range(1, 8):
    dados.append(int(input(f'digite o {c}° numero: ')))
valores.append(dados[:])
print(valores)
for n in dados:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
valores.append(impar[:])
valores.append(par[:])
print(valores)
