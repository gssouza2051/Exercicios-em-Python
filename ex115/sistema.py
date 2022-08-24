'''criando um Menu'''
from ex115.lib.interface import *
from ex115.lib.arquivo import *

arq='cursoemvideo.txt'
if not  arquivoexiste(arq):
    criararquivo(arq)
from time import sleep
while True:
    resposta=menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do sistema'])
    if resposta==1:
        #opção de listar o conteudo do arquivo
        lerarquivo(arq)
    elif resposta == 2:
        #opção de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome=str(input('Nome: '))
        idade=leiaint('Idade: ')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        #opção de sair do sistema
        cabeçalho('Saindo do sistema...Até logo')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(2)
