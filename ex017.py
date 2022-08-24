'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa'''
import math
co=float(input('Qual valor do cateto oposto? '))
ca=float(input('Qual valor do cateto adjascente? '))
hi=math.hypot(co,ca)
print('o comprimento da hipotenusa é {:.2f} '.format(hi))
'''ou
co=float(input('Qual valor do cateto oposto? '))
ca=float(input('Qual valor do cateto adjascente? '))
hi=(co**2+ca**2)**(1/2)
print('o comprimento da hipotenusa é {:.2f} '.format(hi))
'''