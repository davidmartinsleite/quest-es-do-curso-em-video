# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário
# para a compra de uma casa. Pergunte o valor da casa, o salário do comprador
# e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do
# salário ou então o empréstimo será negado.

emprestimo = int(input('qual o valor do emprestimo desejado: '))
salario = int(input('qual o valor do seu salario:'))
anos = int(input('em quantos anos você quer pagar o emprestimo? '))
meses = anos * 12
if emprestimo / meses > salario * 0.3:
    print('o valor de {:.2f} por mês não pode ser aprovado'.format(emprestimo / meses))
else:
    print('o valor de {:.2f} por mês foi aprovado parabens!'.format(emprestimo / meses))
