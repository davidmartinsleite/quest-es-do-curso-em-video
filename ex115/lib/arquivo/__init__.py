from ex115.lib.interface import *


def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')  #vamos tentar abrir para read = "r" e text t "t"
        a.close()  # fecha o arquivo
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')  #aqui vamos criar um aquivo de texto, write = "w"
        # text = "t" e caso o arquivo NÃO EXISTA o "+" serve para isso!
        a.close()
    except:
        print('ouve um erro na criação do arquivo!')
    else:
        print(f'arquivo {nome} foi criado com sucesso')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')  # NOTA não esquecer o nome do arquivo!
    except:
        print('erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        #print(a.readlines())
        # não é "readline" é "readlines" pra ler tudo
        # NOTA o "readlines" lê como LISTA caso queira ler
        # como esteja use o "read()"
        #print(a.read())  # arqui ele lê o arquivo inteiro
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            #NOTA: foi colocado um "\n" no final de cada cadastro
            # na função cadastrar, esse "replace" é para remover esse "\n"
            # que foi colocado
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()  # dando certo ou dando errado vamos fechar o arquivo


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')  # apend = "a", serve para colocar dados
        # dentro do arquivo
    except:
        print('houve um erro na abertura do arquivo')
    else:
        try:  # esse try vem depois de tentar um try com sucesso atrás
            a.write(f'{nome};{idade}\n')
        except:
            print('houve um erro na hora de escrever os dados')
        else:
            print(f'novo registro de {nome} adicionado')
            a.close()
