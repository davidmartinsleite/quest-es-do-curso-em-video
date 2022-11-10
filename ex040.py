# Exercício Python 040: Crie um programa que leia duas notas de
# um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
#
# – Média abaixo de 5.0: REPROVADO
#
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
#
# – Média 7.0 ou superior: APROVADO

nota01 = float(input('digite a primeira nota: '))
nota02 = float(input('digite a segunda nota: '))

media = (nota01 + nota02)/2
if 0.0 <= media <= 5.0:
    print('a nota de {} não é suficiente, infelizmente você está reprovado'.format(media))
elif 5.0 <= media <= 6.9:
    print('a nota de {} não é suficiente, más você está de recuperação'.format(media))
elif 7.0 <= media <= 10.0:
    print('parabens! a nota de {} lhe torna aprovado!'.format(media))
else:
    print('valor invalido')
