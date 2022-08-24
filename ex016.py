#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
n=float(input('Digite um número:'))
s= math.trunc(n)
print('o número {} tem sua porção inteira como : {}'.format(n,s))
#ou
#import math
#n=float(input('Digite um número:'))
#print('o número {} tem sua porção inteira como : {}'.format(n,math.trunc(n)))