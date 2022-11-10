# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se
# ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
#
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM
# A DATA DA MARATONA.

nova_frase = ''
frase = input('digite uma frase: ').strip().upper()
palavras = frase.split()
# ele vai juntar tudo que tenha nada '' entre eles, esse nada foi criado pelo 'split'
junto = ''.join(palavras)
inverso = ''
# podemos subistituir o 'for' por uma estrutura de fatiamento
# inverso = junto[::-1]
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('o inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('temos um palídromo!')
else:
    print('a frase digitada não é um palídromo!')
