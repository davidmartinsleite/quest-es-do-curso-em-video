# Exercício Python 059: Crie um programa que leia dois valores e mostre um
# menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('digite o primeiro valor: '))
n2 = int(input('digite o segundo valor: '))
print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
opcoe = int(input('selecione uma opção: '))
while opcoe != 5:
    if opcoe == 1:
        print('a soma de {}+{}={}'.format(n1, n2, n1+n2))
    elif opcoe == 2:
        print('a multiplicação de {}X{}={}'.format(n1, n2, n1 * n2))
    elif opcoe == 3:
        if n1 > n2:
            print('o maior numero entre {} e {} é: {}'.format(n1, n2, n1))
        elif n1 < n2:
            print('o maior numero entre {} e {} é: {}'.format(n1, n2, n2))
        else:
            print('os numeros são iguais!')
    elif opcoe == 4:
        n1 = int(input('digite o primeiro valor: '))
        n2 = int(input('digite o segundo valor: '))
    else:
        print('opção invalida!')
    opcoe = int(input('selecione uma opção: '))
print('obrigado por usar o programa!')
