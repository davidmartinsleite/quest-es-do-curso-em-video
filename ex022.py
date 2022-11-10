nomeCompleto = input('escreva o nome completo: ')
print(nomeCompleto.upper())
print(nomeCompleto.lower())
espacos = nomeCompleto.count(' ')
letras = len(nomeCompleto)
print('temos {} letras'.format(letras - espacos))
primeiroNome = nomeCompleto.split()
primeiroNome = primeiroNome[0]
print('{} tem {} letras'.format(primeiroNome, len(primeiroNome)))

