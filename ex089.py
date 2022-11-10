# Exercício Python 089: Crie um programa que leia nome e duas
# notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e
# permita que o usuário possa mostrar as notas de cada aluno
# individualmente.

alunos = []
dados = []
continuar = 'S'
numero = referencia = 0
while continuar == 'S':

    dados.append(numero)
    dados.append(str(input('nome: ')))
    dados.append(int(input('primeira nota: ')))
    dados.append(int(input('segunda nota: ')))
    alunos.append(dados[:])
    numero += 1
    dados.clear()
    while True:
        continuar = input('deseja continuar[S/N/? ').strip().upper()[0]
        if continuar in 'SN':
            break
        else:
            print('valor invalido...')
print('No.    NOME      MÉDIA')
print('-'*25)
for a in alunos:
    media = (a[2]+a[3])/2
    print(f'{a[0]:<3} {a[1]:^10} {media:>5}')
while True:
    referencia = int(input('mostrar as notas de qual aluno? (999 interrompe): '))
    if referencia in range(len(alunos)):
        print(f'notas de {alunos[referencia][1]} são : [{alunos[referencia][2]}] '
              f'e [{alunos[referencia][3]}]')
    elif referencia == 999:
        break
    else:
        print('valor invalido...')
print('fim do programa')