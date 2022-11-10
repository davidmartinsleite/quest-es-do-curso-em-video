teste = list()
teste.append('gustavo')
teste.append(40)
print(teste)
galera = list()
galera.append(teste[:])# o [:] serve para fazer uma copia, caso n coloque ele vai conectar o
# teste ao galera, e caso vc mude um elemento de um o outro tbm vai receber a mudança
print(galera)
teste[0] = 'maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera = [['jogão', 19], ['ana', 33], ['jogaquim', 13], ['maria', 45]]
print(galera)
print(galera[2])
print(galera[1][0])

for p in galera:
    print(p)
for p in galera:
    print(p[0])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')




galera2 = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('nome: ')))
    dado.append(int(input('idade: ')))
    galera2.append(dado[:])# essa função adiciona uma lista dentro de uma outra lista
    print(dado)
    dado.clear()
    print(dado)
print(galera2)
menor = maior = 0
for p in galera2: # o "p" vai assumir os valoes dentro da lista, nesse caso vai mostrar
    # a lista que está contida dentro da lista
    if p[1] >= 21:
        print(f'{p[0]} e maior de idade')
        maior += 1
    else:
        print(f'{p[0]} e menor de idade')
        menor += 1
print(f'temos {maior} pessoas maior de idade e {menor} menor de idade')
