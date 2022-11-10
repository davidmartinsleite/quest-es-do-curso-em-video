velocidade = int(input('em qualquer velocidade o carro se encontra? '))
if velocidade <= 80:
    print('você passou na velocidade permitida')
else:
    print('você foi multado! você vai pagar um valor de {} reais por trafegar '
          'na velocidade de {}km/h'.format(((velocidade-80)*7), velocidade))
