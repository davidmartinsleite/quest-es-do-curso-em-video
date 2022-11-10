# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaint():
    while True:
        try:
            inteiro = input('digite um numero inteiro: ')
            inteiro = int(inteiro)
        except KeyboardInterrupt:
            print('\no usuario preferiu não informar os dados')
        except:
            print('\033[31minvalido...\033[m ')
        else:
            return inteiro


def leiafloat():
    while True:
        try:
            real = input('digite um numero real: ')
            real = float(real)
        except KeyboardInterrupt:
            print('\no usuario preferiu não informar os dados')
            return 0
        except:
            print('\033[31minvalido...\033[m ')
        else:
            return real



inteiro = leiaint()
print(inteiro)

real = leiafloat()
print(real)
