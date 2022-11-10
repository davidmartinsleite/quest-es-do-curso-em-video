# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as
# funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas
# funções.

from exmodulos import aumentar, diminuir, dobro, metade

valor = int(input('digite o preço R$: '))
print(f'aumentando 10% temos R$: {aumentar(valor)}')
print(f'diminuindo 10% temos R$: {diminuir(valor)}')
print(f'o dobro de {valor} é {dobro(valor)}')
print(f'o metade de {valor} é {metade(valor)}')
