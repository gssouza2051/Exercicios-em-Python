'''Crie um programa que faça o computador jogar Jokenpô com você.'''
from random import randint
itens=('Pedra','Papel','Tesoura')
computador=randint(0,2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador=int(input('Qual a sua jogada?'))
print('-='*11)
print('Computador jogou {} '.format(itens[computador]))
print('jogador jogou {} '.format(itens[jogador]))
print('-='*11)
if computador ==0:    #computador jogou pedra
    if jogador ==0:
        print('EMPATE')
    elif jogador ==1:
        print('Jogador VENCE')
    elif jogador ==2:
        print('Computador VENCE')
    else:
        print('Jogada Inválida!')
elif computador ==1:  #computador jogou papel
    if jogador ==0:
        print('Computador VENCE')
    elif jogador ==1:
        print('EMPATE')
    elif jogador ==2:
        print('Jogador VENCE')
    else:
        print('Jogada Inválida!')
elif computador ==2:  #computador jogou tesoura
    if jogador ==0:
        print('Jogador VENCE')
    elif jogador ==1:
        print('Computador VENCE')

    elif jogador ==2:
        print('EMPATE')
    else:
        print('Jogada Inválida!')
