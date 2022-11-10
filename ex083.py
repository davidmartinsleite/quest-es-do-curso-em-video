# Exercício Python 083: Crie um programa onde o usuário digite
# uma expressão qualquer que use parênteses. Seu aplicativo
# deverá analisar se a expressão passada está com os parênteses
# abertos e fechados na ordem correta.

texto = input('digite algo: ')
pilha = []
for simbulo in texto:
    if simbulo == '(':
        pilha.append('(')
    elif simbulo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('sua expreção está correta!')
else:
    print('sua expreção está errada!')
