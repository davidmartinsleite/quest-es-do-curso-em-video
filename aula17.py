# aula referente a listas parte 1

num = [2, 5, 9, 1]
num[2] = 3 # = [2, 5, 3, 1]
# num[4] = 7 erro, pq tem q usar append() para adicionar
num.append(7) # = [2, 5, 3, 1, 7]
num.sort() # = [1, 2, 3, 5, 7]
num.sort(reverse=True) # = [7, 5, 3, 2, 1]
# NOTA: a estrutura qnd modificada ela fica atribuida a lista
len(num) # = 5
num.insert(2, 0) # = [7, 5, 0, 3, 2, 1]
num.pop() # = [7, 5, 0, 3, 2] retirou o ultimo
num.pop(2) # = [7, 5, 3, 2] retirou o da celula 2
num.insert(2, 2) # = [7, 5, 2, 3, 2] adicionou o 2 a celula 2
num.index(5) # = 1
#localiza o PRIMEIRO valor e retorna a celula em que esse valor está
num.remove(2) # = [7, 5, 3, 2] removeu o PRIMEIRO 2 da lista
#NOTA: se tentar remover algo q n existe da um erro, use uma
# função para evitar isso

valores = list()# cria uma lista vazia ou 'valores = []'
valores.append(5)
valores.append(9)
valores.append(4)
# = valores = [5, 9, 4]


for v in valores:#para cada valor em valores faça...
    print(f'{v}...', end='')
for c, v in enumerate(valores):
    print(f'na posição {c} encontrei o valor {v}!')
print('cheguei ao final da lista.')


#conexão de elementos de listas
a = [2, 3, 4, 7]
b = a # aqui vc esta criando uma conexão entre a lista a e b
# loga se vc mudar algo na 'a' vc tbm vai mudar a lsita 'b'
# para fazer uma copia vc pode usar a função b = a[:]
b[2] = 8 # aqui ele vai atribuir o valor 8 na selula 2 no 'a' e no 'b',
# pq eles estão CONECTADOS
print(f'lista A: {a}')
print(f'lista A: {b}')
# lista A: [2, 3, 4, 7]
# lista A: [2, 3, 4, 7]

b = a[:] # aqui 'b' só recebe uma COPIA de 'a'
b[2] = 0
print(f'lista A: {a}')
print(f'lista A: {b}')
# lista A: [2, 3, 8, 7]
# lista A: [2, 3, 0, 7]
