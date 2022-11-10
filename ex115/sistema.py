# Exercício Python 115a: Vamos criar um menu em Python,
# usando modularização.

from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas',
                     'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('opção 1')
        lerarquivo(arq)
    elif resposta == 2:
        cabecalho('opção 2')
        nome = str(input('nome: '))
        idade = leiaint('idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('saindo do sistema até logo')
        break
    else:
        print('\033[31mERRO! Digite uma opção valida!\033[m')
        sleep(1)
