# Exercício Python 067: Faça um programa que mostre a tabuada de
# vários números, um de cada vez, para cada valor digitado pelo
# usuário. O programa será interrompido quando o número solicitado
# for negativo.

while True:
    numero = int(input('digite o número que será visto a tabuada: '))
    for c in range(1, 11):
        resultado = numero * c
        print(f'{c} X {numero} = {resultado}')
    if numero < 0:
        break
print('obrigado por usar o programa')

