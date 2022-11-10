def aumentar(preco=0, taxa=10, formatado=False):
    total = preco + (preco * (taxa / 100))
    return total if formatado is False else moeda(total)


def diminuir(preco=0, taxa=10, formatado=False):
    total = preco - (preco * (taxa / 100))
    return total if formatado is False else moeda(total)


def dobro(preco=0, formatado=False):
    total = preco * 2
    return total if formatado is False else moeda(total)


def metade(preco=0, formatado=False):
    total = preco / 2
    return total if formatado is False else moeda(total)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def escreva(texto):
    tamanho = len(texto) + 4
    print('~'*tamanho)
    print(f'  {texto}')
    print('~'*tamanho)


def resumo(preco, aumento, reducao):
    resultado_aumentado = aumentar(preco, aumento, True)
    resultado_diminuido = diminuir(preco, reducao, True)
    resultado_metade = metade(preco, True)
    resultado_dobro = dobro(preco, True)
    escreva('RESUMO DO VALOR')
    print(f'preço analisado:\t\t{moeda(preco)}')
    print(f'dobro do preço: \t\t{resultado_dobro}')
    print(f'metade do preço:\t\t{resultado_metade}')
    print(f'{aumento}% de aumento:\t\t\t{resultado_aumentado}')
    print(f'{reducao}% de redução:\t\t\t{resultado_diminuido}')


def leiaDinheiro(preco):
    preco = str(preco).strip()
    while True:
        try:
            preco = preco.replace(',', '.')
            preco = float(preco)
        except Exception as erro:
            print(f'problema encontrado foi {erro.__class__}')
            preco = input('\033[31mdigite uma quantidade valida:\033[m ')
        else:
            return preco
