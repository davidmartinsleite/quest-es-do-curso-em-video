# Exercício Python 090: Faça um programa que leia nome e média
# de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.


aluno = {}
for c in range(1):
    aluno['aluno'] = str(input('nome: '))
    aluno['media'] = int(input('media: '))
print('-='*20)
print(f'nome do aluno: {aluno["aluno"]}')
print(f'media do aluno: {aluno["media"]}')
print(aluno['media'])
if aluno['media'] >= 7:
    print('o aluno está aprovado!')
elif 6.7 >= aluno['media'] >= 5:
    print('o aluno está em recuperação!')
else:
    print('o aluno está reprovado...')
