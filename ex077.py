# Exercício Python 077: Crie um programa que tenha uma tupla
# com várias palavras (não usar acentos). Depois disso, você
# deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
            'ESTUDAR', 'PRATICAR', 'TRBALHAR', 'MERCADO', 'PROGRAMADOR',
            'FUTURO')
#ele vai analizar cada palavras e armazenar ela temporariamente em 'c'
for c in palavras:
    print(f'\nna palavra: {c} temos as vogais: ', end='')
    #agora ela vai armazenar cada letra em 'letra', assim eu consigo analisar
    # tudo de forma separada
    for letra in c:
        if letra in 'AEIOU':
            print(letra.lower(), end=' ')
