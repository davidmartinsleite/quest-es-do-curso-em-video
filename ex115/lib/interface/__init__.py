def leiaint(texto):
    while True:
        try:
            inteiro = input(texto)
            inteiro = int(inteiro)
        except KeyboardInterrupt:
            print('\no usuario preferiu não informar os dados')
        except:
            print('\033[31minvalido...\033[m ')
        else:
            return inteiro


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c} - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('digite sua opção: ')
    return opc
