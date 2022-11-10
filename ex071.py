# Exercício Python 071: Crie um programa que simule o funcionamento
# de um caixa eletrônico. No início, pergunte ao usuário qual será
# o valor a ser sacado (número inteiro) e o programa vai informar
# quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

saque = int(input('digite o valor a ser sacado: '))
nota50 = nota20 = nota10 = nota1 = 0
while True:
    if saque >= 50:
        saque -= 50
        nota50 += 1
    elif saque >= 20:
        saque -= 20
        nota20 += 1
    elif saque >= 10:
        saque -= 10
        nota10 += 1
    elif saque >= 1:
        saque -= 1
        nota1 += 1
    elif saque == 0:
        break
print(f'''notas de 50: {nota50} 
notas de 20: {nota20}
notas de 10: {nota10}
moedas de 1: {nota1}''')

