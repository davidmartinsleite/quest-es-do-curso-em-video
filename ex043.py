# Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#
# – IMC abaixo de 18,5: Abaixo do Peso
#
# – Entre 18,5 e 25: Peso Ideal
#
# – 25 até 30: Sobrepeso
#
# – 30 até 40: Obesidade
#
# – Acima de 40: Obesidade Mórbida

altura = float(input('digite sua altura: '))
peso = float(input('digite seu peso: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('o imc de {:.1f} é abaixo do peso'.format(imc))
elif 18.5 <= imc < 25:
    print('o imc de {:.1f} é de peso ideal'.format(imc))
elif 18.5 <= imc < 25:
    print('o imc de {:.1f} é de sobrepeso'.format(imc))
elif 25 <= imc < 40:
    print('o imc de {:.1f} é de obesidade'.format(imc))
elif 50 <= imc:
    print('o imc de {:.1f} é de obesidade mórbida'.format(imc))
else:
    print('valor invalido')
