# Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros
# colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem
# de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ('PAL', 'FLA', 'INT', 'COR', 'FLU', 'CAP', 'CAM', 'SAO', 'AMG', 'FOR',
         'BOT', 'SAN', 'RBB', 'GOI', 'CFC', 'CEA', 'AGO', 'CUI', 'AVA', 'ECJ')
print(f'os primeiros colocados em ordem são: {times[:5]}')
print(f'os ultimos colocados são: {times[-4:]}')
print(f'os times participantes em ordem alfabetica são: {sorted(times)}')
colocacao = times.index('CEA') # localiza a posição q aquele elemento está
print(f'o ceará(CEA) está na posição {colocacao}° do compeonato')

times.count('CEA') #vai contar quantas vezes aquele elemento vai
# aparecer na tupla
