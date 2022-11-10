nome = input('digite o nome? ').upper().strip()
print('a letra A aparece {} vezes na frase'.format(nome.count('A')))
print('a primeira letra A aparece na posição: {}'.format(nome.find('A')))
print('a última letra A aparece na posição: {}'.format(nome.rfind('A')))
