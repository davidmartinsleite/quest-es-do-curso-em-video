n1 = int(input('escreva o primeiro numero: '))
n2 = int(input('escreva o segundo numero: '))
n3 = int(input('escreva o terceiro numero: '))
if n1 < n2 < n3:
    print(n1,n2,n3)
if n1 < n3 < n2:
    print(n1, n3, n2)
if n2 < n1 < n3:
    print(n2, n1, n3)
if n2 < n3 < n1:
    print(n2, n3, n1)
if n3 < n1 < n2:
    print(n3, n1, n2)
if n3 < n2 < n1:
    print(n3, n2, n1)
