# Exercício Python 057: Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação
# novamente até ter um valor correto.


# o '[0]' serve para selecionar o primeiro caracter do texto escrito
sexo = input('diga o sexo da pessoa (M/F): ').strip().upper()[0]
while sexo not in 'MF': #valores q estejam dentro das aspas ativão a condição
    sexo = input('valor incorreto, digite o sexo da pessoa (M/F): ').strip().upper()[0]
