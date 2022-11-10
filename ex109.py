# Exercício Python 109: Modifique as funções que form criadas no desafio
# 107 para que elas aceitem um parâmetro a mais, informando se o valor
# retornado por elas vai ser ou não formatado pela função moeda(),
# desenvolvida no desafio 108.

from exmodulos import aumentar, diminuir, dobro, metade, moeda

valor = int(input('digite o preço R$: '))
taxa = int(input('difite a taxa: '))
# NOTA: perceba que temos uma função dentro de outra função
print(f'aumentando {taxa}% temos R$: {aumentar(valor, taxa, True)}')
print(f'diminuindo {taxa}% temos R$: {diminuir(valor, taxa, True)}')
print(f'o dobro de {moeda(valor)} é {dobro(valor, True)}')
print(f'o metade de {moeda(valor)} é {metade(valor, True)}')
