# NOTA: perceba que a importação foi com "from", isso foi por conta das
# subpastas que foram criadas, isso não é um Módulo, isso é um Pacote
# caso tivesse um arquivo no com as funções dentra da mesma pagina isso
# seria um módulo, que muitas vezes é suficiente e é oq vai ser mais usado
from aula22modulos import numeros

num = int(input('digite um valor: '))
fat = numeros.fatorial(num)
print(f'o fatorial de {num} é {fat}.')
print(f'o dobro de {num} é {numeros.dobro(num)}')
print(f'o triplo de {num} é {numeros.triplo(num)}')
