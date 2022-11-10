# Exercício Python 093: Crie um programa que gerencie o
# aproveitamento de um jogador de futebol. O programa vai ler
# o nome do jogador e quantas partidas ele jogou. Depois vai
# ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total
# de gols feitos durante o campeonato.

jogador = {}
gols = []
jogador['nome'] = input('nome do jogador: ')
jogador['partidas'] = int(input(f'quantas perdidas {jogador["nome"]} jogou? '))
for p in range(jogador['partidas']):
    #gol = int(input(f'quantos gols {jogador["nome"]} fez na {p+1}° partida? '))
    gols.append(int(input(f'quantos gols {jogador["nome"]} fez na {p+1}° partida? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'o campo {k} tem valor: {v}')
print('-='*30)
print(f'o jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas')
for p in range(jogador['partidas']):
    print(f'na {p+1}° partida fez {jogador["gols"][p]} gols')
print(f'foi um total de {jogador["total"]} gols')
