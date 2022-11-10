# Exercício Python 104: Crie um programa que tenha a função leiaInt(),
# que vai funcionar de forma semelhante 'a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')

def leiaint(texto):
    while True:
        numero = input(texto)
        if numero.isnumeric():
            numero = int(numero)
            break
        else:
            print('\033[31merro, o dado não é um numero inteiro\033[38m')
    return numero


n = leiaint('digite um numero: ')
print(f'você digitou o numero {n}')
