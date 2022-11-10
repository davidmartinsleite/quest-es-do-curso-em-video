pessoas = {'nome': 'gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas) # {'nome': 'gustavo', 'sexo': 'M', 'idade': 22}
# print(pessoas) dá erro, pq n existe pessoas 0
print(pessoas['nome']) # gustavo
print(f'o {pessoas["nome"]} tem {pessoas["idade"]} anos.')#o gustavo tem 22 anos.
#NOTA: as aspas são duplas e n simples
print(pessoas.keys())#dict_keys(['nome', 'sexo', 'idade'])
print(pessoas.values())#dict_values(['gustavo', 'M', 22])
print(pessoas.items())#dict_items([('nome', 'gustavo'), ('sexo', 'M'), ('idade', 22)])

for k in pessoas.keys():
    print(k) # nome \n sexo \n idade

for k in pessoas.values():
    print(k) # gustavo \n M \n 22

for k in pessoas.items():
    print(k) # ('nome', 'gustavo') \n ('sexo', 'M') \n ('idade', 22)

#metodo para visualização TOTAL de dados
for k, v in pessoas.items():
    print(f'{k} = {v}') # nome = gustavo \n sexo = M \n idade = 22


del pessoas['sexo'] #deletar
for k, v in pessoas.items():
    print(f'{k} = {v}') # nome = gustavo \n idade = 22

pessoas['nome'] = 'leandro' #modificar
for k, v in pessoas.items():
    print(f'{k} = {v}') # nome = leandro \n idade = 22

pessoas['peso'] = 98.5 # adicionar
for k, v in pessoas.items():
    print(f'{k} = {v}') # nome = leandro \n idade = 22 \n peso = 98.5


#criando uma lista com discionarios
brasil = []
estado1 = {'uf': 'rio de janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'são paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)#{'uf': 'rio de janeiro', 'sigla': 'RJ'}
print(estado2)#{'uf': 'são paulo', 'sigla': 'SP'}
print(brasil)#[{'uf': 'rio de janeiro', 'sigla': 'RJ'}, {'uf': 'são paulo', 'sigla': 'SP'}]
print(brasil[0])#{'uf': 'rio de janeiro', 'sigla': 'RJ'}
print(brasil[1]['uf']) #são paulo



# acrecentando dados ao discionario INDEPENDENTES
estado = {}
brasil2 = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('sigla da estado: '))
    #brasil2.append(estado[:]) caso vc queira fazer isso vai dar erro, pq n pode fatiar um dicionario
    brasil2.append(estado.copy())#forma correta
# mostrando na tela de formas diferentes...
for e in brasil2:
    print(e) #{'uf': 'sampa', 'sigla': 'sp'} \n {'uf': 'rio', 'sigla': 'rj'} \n {'uf': 'ceara', 'sigla': 'ce'}

for e in brasil2:
    for k, v in e.items():
        print(f'o campo {k} tem valor {v}.')
            #o campo uf tem valor ceara.
            #o campo sigla tem valor ce.
            #o campo uf tem valor piaui.
            #o campo sigla tem valor pi.
            #o campo uf tem valor bahia.
            #o campo sigla tem valor bh.

for e in brasil2:
    for v in e.values():
        print(v, end=' ')
    print()
    #ceara ce
    #paraiba pa
    #bahia bh





