# Exercício Python 44: Elabore um programa que calcule o valor a ser pago
# por um produto, considerando o seu preço normal e condição de pagamento:
#
# – à vista dinheiro/cheque: 10% de desconto
#
# – à vista no cartão: 5% de desconto
#
# – em até 2x no cartão: preço formal
#
# – 3x ou mais no cartão: 20% de juros

produto = float(input('qual o valor do produto? '))
pagamento = int(input('''formas de pagamento
 [ 1 ] à vista dinheiro/cheque
 [ 2 ] à vista no cartão
 [ 3 ] 2x no cartão
 [ 4 ] 3x ou mais no cartão
 opção de pagamento: '''))
if pagamento == 1:
    print('o valor de {} fica por {} com o desconto à vista'.format(produto, produto * 0.9))
elif pagamento == 2:
    print('o valor de {} fica por {} com o desconto á vista no cartão'.format(produto, produto * 0.95))
elif pagamento == 3:
    print('o valor de {} fica divido em 2x de {}'.format(produto, produto / 2))
elif pagamento == 4:
    pagamento = int(input('quantas parcelas? '))
    print('sua compra de {} será divida em {}x no valor de {} com juros\n'
          'com custo total de {} reais'.format(produto, pagamento, (produto * 1.2) / pagamento, produto * 1.2))

