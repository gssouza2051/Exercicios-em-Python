'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.'''
a=float(input('Digite o comprimeiro da primeira reta:'))
b=float(input('Digite o comprimeiro da segunda reta:'))
c=float(input('Digite o comprimeiro da terceira reta:'))
if a<b+c and b<a+c and  c<a+b:
    print('As retas formam um triângulo!')
else:
    print('As retas não formam um triangulo!')