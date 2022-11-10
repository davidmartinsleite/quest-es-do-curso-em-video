# Exercício Python 105: Faça um programa que tenha uma função notas()
# que pode receber várias notas de alunos e vai retornar um dicionário
# com as seguintes informações:
#
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
#
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.


def notas(*notas, situacao=False):
    '''
    sistema que gera a media de notas da classe, notas menores que 4 ruim, até 6 rezoavel e mais
    que 8 nota boa
    :param notas: recebe a quantidade de notas dinamicas e gera uma media de todas
    :param situacao: caso a opção de situação estaja habilitada gera o relatorio da situação
    da sala
    :return: uma lista com os principais dados
    '''
    boletim = {}
    provas = []
    for nota in notas:
        provas.append(nota)
    #provas.sort()
    media = sum(provas) / len(provas)

    boletim['total'] = len(provas)
    boletim['maior'] = max(provas)
    boletim['menor'] = min(provas)
    boletim['media'] = media

    if situacao:
        if media < 4:
            boletim['situacao'] = 'ruim'
        elif media < 6:
            boletim['situacao'] = 'razoavel'
        elif media < 8:
            boletim['situacao'] = 'boa'

    return boletim


resposta = notas(5.5, 7, 8.5, 2, situacao=True)
print(resposta)
#help(notas)
