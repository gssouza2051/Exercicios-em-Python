'''Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''
numero=int(input('Digite um valor qualquer :'))
resultado= numero % 2
if resultado==0:
    print('o número  {} é par'.format(numero))
else:
    print('o número {} é ímpar'.format(numero))
