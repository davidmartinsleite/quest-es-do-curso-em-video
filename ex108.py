# Exercício Python 108: Adapte o código do desafio #107, criando uma
# função adicional chamada moeda() que consiga mostrar os números como
# um valor monetário formatado.

from exmodulos import aumentar, diminuir, dobro, metade, moeda

valor = int(input('digite o preço R$: '))
taxa = int(input('difite a taxa: '))
# NOTA: perceba que temos uma função dentro de outra função
print(f'aumentando {taxa}% temos R$: {moeda(aumentar(valor, taxa))}')
print(f'diminuindo {taxa}% temos R$: {moeda(diminuir(valor, taxa))}')
print(f'o dobro de {moeda(valor)} é {moeda(dobro(valor))}')
print(f'o metade de {moeda(valor)} é {moeda(metade(valor))}')

