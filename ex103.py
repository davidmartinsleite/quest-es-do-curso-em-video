# Exercício Python 103: Faça um programa que tenha uma função
# chamada ficha(), que receba dois parâmetros opcionais: o nome
# de um jogador e quantos gols ele marcou. O programa deverá ser
# capaz de mostrar a ficha do jogador, mesmo que algum dado não
# tenha sido informado corretamente.


def ficha(jogador='ideterminado', gols=0):
    print(f'o jogador {jogador} fez {gols} gols')


jogador = input('nome do jogador: ').strip()
gols = input('quantidade de gols feitos na carreira: ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if jogador == '':
    ficha(gols=gols)
else:
    ficha(jogador, gols)
