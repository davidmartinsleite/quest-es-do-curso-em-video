# essa função mostrar qualquer função interna do python,
# tbm pode mostrar funções criados por vc
#help()

help(print())
print(input.__doc__)


# isso é uma docstring serve para passar instruções referentes a função contruida
def contador(i, f, p):
    '''
    sistema de contagem com passo definido por você e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: não tem retorno
    '''
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')


help(contador)
contador(2, 10, 2)  # 2 4 6 8 10 FIM!


# parametros opcionais, NOTA isso não funciona para mais parametros...
# para isso use "* parametros"
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'a soma vale {s}')


somar(3, 2, 5)  # a soma vale 10
somar(8, 4)  # a soma vale 12


# escopo de variaveis
def funcao():
    n1 = 4
    print(f'n1 dentro vale {n1}')


n1 = 2
funcao()
print(f'n1 fora vale {n1}')


# variavel global
def teste(b):
    global a  # essa variavel conecta as minhas variaveis internas com as esternas
    a = 8
    b += 4
    c = 2
    print(f'a dentro vale {a}')  # a dentro vale 8
    print(f'b dentro vale {b}')  # b dentro vale 9
    print(f'c dentro vale {c}')  # c dentro vale 2


a = 5
teste(a)
print(f'a fora vale {a}')  # a fora vale 5, com a global: a fora vale 8


# retorno de  valores
def somando(a=0, b=0, c=0):
    s = a + b + c
    # print(f'a soma vale {s}') em vez de usar essa saida podemos usar um return
    return s


resposta = somando(3, 2, 5)  # perceba q eu joguei pra dentro de uma variavel
# agora a resposta
print(resposta)
# tabem posso retornar varias variaveis...
r1 = somando(3, 2, 5)  # r1 = 10
r2 = somando(1, 7)  # r2 = 8
r3 = somando(4)  # r3 = 4


# pratica!
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('digite um número: '))
print(f'o fatorial de {n} é igual a {fatorial(n)}')
print('-'*15)

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'os resultados são: {f1} {f2} {f3}')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('digite um numero para saber se é par ou impar: '))
if par(num):
    print('é par')
else:
    print('não é par')
