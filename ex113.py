'''Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação
de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''
def leiaint(msg):
    while True:
        try:
            n=int(input(msg))
        except(ValueError,TypeError):
            print('\033[31mERRO: Por favor,digite um número inteiro válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31Usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n=float(input(msg))
        except(ValueError,TypeError):
            print('\033[31mERRO: Por favor,digite um número real válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31Usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


n1=leiaint('Digite um Inteiro: ')
n1=leiafloat('Digite um Real: ')
print(f'O valor digitado inteiro foi {n1} e o real foi {n2}')

