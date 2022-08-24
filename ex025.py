'''Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.'''
nome=str(input('Digite seu nome todo : ')).strip()
print('seu nome tem Silva?  {}'.format('silva' in nome.lower()))