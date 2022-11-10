# nessa atividade temos um redutor de casa decimais para evitar
# grandes numeros a semrem exibidos "{:.3f}" isso serve para para ter
# três casa depois do ponto flutuantes

medida = float(input('digite uma medida em metros para ser convertida: '))
print('a medidade em metros é: {:.2f}M \na medida em centimetros é {:.2f}cm '
      '\na medida em milimetros é {:.3f}mm'.format(medida, medida * 10,medida * 100))