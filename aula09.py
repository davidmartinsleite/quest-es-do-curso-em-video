frase = 'curso em video python'
print(len(frase))
print(frase[0:15])
print('a letra o parece: ', frase.count('o'))
print(len(frase[0:15]))
print(frase.replace('python', 'C++'))
dividido = frase.split()
juntando = '-'.join(frase)
print(juntando)
print('a palava video foi localizada na lacuna: ', frase.find('video'))
print(dividido)
print(dividido[2])
print(dividido[2][3])

