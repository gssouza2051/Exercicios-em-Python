"""Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo"""
import math
a=float(input('Digite um angulo'))
seno=math.sin(math.radians(a))
cos=math.cos(math.radians(a))
tang=math.tan(math.radians(a))
print('O valor do angulo {:.1f} no seno é de {:.1f} \n Do cosseno é de {:.1f} \n E da tangente {:.1f} !'.format(a,seno,cos,tang))
