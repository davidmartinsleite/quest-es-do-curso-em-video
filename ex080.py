# Exercício Python 080: Crie um programa onde o usuário possa
# digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.
valor = []
for c in range(0 ,5):
    dado = int(input('digite um valor: '))
    if c == 0:
        valor.append(dado)
        print('o primeiro')
    elif dado >= valor[-1]:
        valor.append(dado)
        print('adiciona no final')
    else:
        pos = 0
        while pos < len(valor):# para avaliar o meio (que é o real problema)
            # é feito uma varredura afim de ir comparando os valores de "dado" com as celulas
            if dado <= valor[pos]:# quando a dado é maior ou igual ao valor contido naquela celula
                valor.insert(pos, dado)# ele é inserido logo ai, ultiliznado ma mesma variavel de pos
                print('adiciona no meio')
                break
            pos += 1
print(valor)
