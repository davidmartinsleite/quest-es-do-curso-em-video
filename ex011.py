altura = float(input('programa para quantificar tinta ultilizada! \n'
                     'insira a altura da parede a ser pintada: '))
largura = float(input('insira agora a largura da parede a ser pintada :'))
area = altura * largura
tinta = area / 2
print('a área de {}M X {}M é {}M². ela ultiliza de {} Litros de '
      'tinta'.format(altura, largura, area, tinta))
