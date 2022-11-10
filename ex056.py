# Exercício Python 56: Desenvolva um programa que leia o nome, idade e
# sexo de 4 pessoas. No final do programa, mostre: a média de idade do
# grupo, qual é o nome do homem mais velho e quantas mulheres têm menos
# de 20 anos.
media = 0
maisvelho = 0
mulheres = 0
for pessoa in range(1, 5):
    print('#### {}° pessoa ####'.format(pessoa))
    nome = input('nome: ')
    idade = int(input('idade: '))
    media += idade
    sexo = input('sexo(M/F): ').strip().upper()
    if sexo == 'M' and idade > maisvelho:
        velho = nome
        maisvelho = idade
    if sexo == 'F' and idade < 20:
        mulheres += 1
print('a media da idade do grupo é {:.1f} anos'.format(media / pessoa))
print('o nome do homem mais velho do grupo é {}, ele tem {} anos'.format(velho, maisvelho))
print('existem {} mulheres com menos de 20 anos no grupo'.format(mulheres))
