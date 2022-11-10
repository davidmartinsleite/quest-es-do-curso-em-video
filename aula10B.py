nota01 = float(input('digite a primeira nota: '))
nota02 = float(input('digite a segunda nota: '))
media = (nota01 + nota02) / 2
print('a media da nota é ', media)
if media >= 6.0:
    print('você foi aprovado, parabens')
else:
    print('infelizmente você ficou de recuperação, estude mais')
