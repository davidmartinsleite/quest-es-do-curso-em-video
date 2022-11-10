# Exercício Python 079: Crie um programa onde o usuário possa
# digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente.

valores = list()
continuar = 'S'
while continuar == 'S':
    dado = int(input('digite um valor para a lista: '))
    if dado not in valores:  # essa condição evita de entrar valoes que já foram inseridos
        # anteriormente, caso queira é so tirar essa condição que ele adiciona tudo
        valores.append(dado)

    while True:
        continuar = input('deseja continuar[S/N/? ').strip().upper()[0]
        if continuar in 'SN':
            break
        else:
            print('valor invalido...')
print(valores)
valores.sort()
print(valores)
