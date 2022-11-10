try:  # a condição que ele vai tentar, caso n consiga ele cai no "except:"
      # ele vai verificar TUDO que esteja dentro do "try:"
    a = int(input('numerador: '))
    b = int(input('denominador: '))
    r = a / b
except:  # caso não algo dê um erro no try ele aplica as funções contidas no "except:"
    print('tivemos um problema')
else:  # caso dê CERTO ele pode apresentar esse codigo(não obrigatorio)
    print(f'o resultqado é {r:.1f}')
finally:#o"finally:"vai apresentar um codigo INDEPENDENTE DO RESULTADO (não obrigatorio)
    print('fim do program')


# você pode usar essas estruturas para realizar debug do codigo, afim de localiza-los
print('agora o mesmo programa com diagnostico do erro')
try:
    a = int(input('numerador: '))
    b = int(input('denominador: '))
    r = a / b
except Exception as erro: # define a qual eceção está sendo
    print(f'problema encontrado foi {erro.__class__}') # aqui ele atribui a classe
    # do erro, poder ser <class 'ValueError'> ou <class 'ZeroDivisionError'>, por ai vai...
else:
    print(f'o resultqado é {r:.1f}')
finally:
    print('fim do program')

# NOTA: o mesmo "try" pode ter varios "except": "except TypeError:" ou "except ValueError"
# por ai vai...
print('o mesmo programa com mais diagnosticos de erros')
try:
    a = int(input('numerador: '))
    b = int(input('denominador: '))
    r = a / b
# nesses casos tempos respostas personalizadas para cada tipo de erro que possa existir
except (ValueError, TypeError):  # perceba que nesse caso eu montei 2 erros a serem vistos
    print('tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('não é possivel dividir um numero por zero')
except KeyboardInterrupt:
    print('o usuario preferiu não informar os dados')
except Exception as erro:
    print(f'o erro encontrado foi {erro.__cause__}')
else:
    print(f'o resultqado é {r:.1f}')
finally:
    print('fim do program')
