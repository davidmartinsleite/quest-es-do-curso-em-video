# Exercício Python 101: Crie um programa que tenha uma função chamada
# voto() que vai receber como parâmetro o ano de nascimento de uma
# pessoa, retornando um valor literal indicando se uma pessoa tem
# voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.



def voto():
    import datetime # montar as funções internar economiza memoria do sistema
    ano_atual = datetime.datetime.today().year  # más só servem dentro das funções
    ano = int(input('em que ano você nasceu? '))
    idade = ano_atual - ano
    if idade < 16:
        return f'com {idade} você não tem idade para votar'
    elif idade < 18:
        return f'como {idade} o voto não é obrigatorio'
    elif idade < 70:
        return f'com {idade} o voto é obrigatorio !'
    else:
        return f'mcom {idade} você não é obrigado a votar'

print(voto())