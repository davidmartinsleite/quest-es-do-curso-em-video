# Exercício Python 095: Aprimore o desafio 93 para que ele
# funcione com vários jogadores, incluindo um sistema de
# visualização de detalhes do aproveitamento de cada jogador.
time = []
jogador = {}
gols = []
codigo = 0
while True:
    nome = input('nome do jogador: ')
    partidas = int(input(f'quantas perdidas {nome} jogou? '))
    for partida in range(partidas):
        gols.append(int(input(f'quantos gols {nome} fez na {partida+1}° partida? ')))

    jogador['codigo'] = codigo
    jogador['nome'] = nome
    jogador['partidas'] = partidas
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    codigo += 1
    gols.clear()
    time.append(jogador.copy())

    while True:
        continuar = input('continua? [S/N] ').strip().upper()
        if continuar in 'SN':
            break
        else:
            print('dados invalidos...')
    if continuar == 'N':
        break

print('-='*22)
print('cod  nome          gols               total')
print('-'*44)
for jogador in time:
    print(f'{jogador["codigo"]:<3} {jogador["nome"]:<14} '
          f'{str(jogador["gols"]):<18} {jogador["total"]:3>}')

while True:
    codigo_jogador = int(input('mostrar o detalhamento de qual jogador? (999 interrompe) '))
    if codigo_jogador == 999:
        break
    if codigo_jogador in range(len(time)):
        print(f'levantamento do jogador {time[codigo_jogador]["nome"]}')
        for p, g in enumerate(time[codigo_jogador]['gols']): # enumerate ajuda a não precisar
            # de um contador, ele retorna o valor e uma contagem, no caso aqui ele retorna
            # 0, gols \n 1, gols ...
            print(f'no {p+1}° jogo fez {g} gols')
    else:
        print('valor invalido...')
