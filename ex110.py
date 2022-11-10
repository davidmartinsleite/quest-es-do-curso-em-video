# Exercício Python 110: Adicione o módulo moeda.py criado nos desafios
# anteriores, uma função chamada resumo(), que mostre na tela algumas
# informações geradas pelas funções que já temos no módulo criado até aqui.

from exmodulos import resumo

valor = int(input('digite o preço R$: '))
aumento = int(input('defina a taxa de aumento: '))
reducao = int(input('defina a taxa de redução: '))

resumo(valor, aumento, reducao)
