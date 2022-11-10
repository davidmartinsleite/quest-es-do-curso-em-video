def titulo(msg):
    print('-'*30)
    print(msg)
    print('-'*30)


titulo('       curso em video    ')


def soma(a, b):
    s = a + b
    print(s)


soma(4, 5)


# caso queira fazer valores dinamicos vc pode usar uma variavel com "*" para
# criar uma variavel dinamica, ele vai ser uma TUPLA ex. "*num"
def contador(*num):
    tam = len(num)
    print(f'recebi os valores {num} e são ao todo {tam} números')


contador(1, 2, 3, 4)
contador(2, 4, 6)


# tambem pode pegar uma LISTA e usar em uma função para issso vc pode
# simplismente jogar a lista diretamente para a função
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2 # "*= 2" essa função dobra, poderia triplicar "3",
        # por ai vai...
        pos += 1


valores = [7, 2, 5, 0, 4]
print(valores)
dobra(valores) # perceba que aqui eu simplismente joguei a lista na função
print(valores)


#podemos melhorar a função de soma que foi feita logo a cima a fim de se
# tornar tambem uma função dinamica
def novasoma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'somando os valores {valores} temos {s}')


novasoma(5, 2)
novasoma(2, 9, 4)
