# Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem
# de apresentação de trabalhos dos alunos. Faça um programa que leia o nome
# dos quatro alunos e mostre a ordem sorteada.

from random import shuffle # dessa vez foi utilizado a biblioteca especifica para evitar gastos com memoria
n1 = input('primeiro aluno: ')
n2 = input('segundo aluno: ')
n3 = input('terceiro aluno: ')
n4 = input('quarto aluno: ')
lista = [n1, n2, n3, n4]# essa linha cria uma lista (arraw)
shuffle(lista)#aqui foi removido o "random." pq foi utilizado especifico o shuffle
# aqui não foi nescessario atribuição
# pq ele embaralhou(shuffle) a propria lista
print('o aluno escolhido foi {}'. format(lista))
