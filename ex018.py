import math
angulo = float(input('digite o ângulo desejado: '))
radiano = math.radians(angulo)
seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)
print('o angulo de {} tem seno de {:.2f}'.format(angulo,seno))
print('o angulo de {} tem cosseno de {:.2f}'.format(angulo,cosseno))
print('o angulo de {} tem tangente de {:.2f}'.format(angulo,tangente))
