'''Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
 qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''
from random import randint
computador = randint(0,5) #pro computador pensar
print('vou pensar em numero entre 0 a  5,tente adivinhar:')
jogador=int(input('em que numero eu pensei?'))  #pro jogador adivinhar
if jogador==computador:
    print('PARABENS,voce acertou!!')
else:
    print('Você errou,fica para próxima')

