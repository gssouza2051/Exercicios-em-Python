'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes'''
a=float(input('Digite o comprimeiro da primeira reta:'))
b=float(input('Digite o comprimeiro da segunda reta:'))
c=float(input('Digite o comprimeiro da terceira reta:'))
if a<b+c and b<a+c and  c<a+b:
    print('As retas formam um triângulo!')
    if a ==b == c :
        print('O triângulo formado é EQUILÁTERO')
    elif a !=b != c != a:
        print('O triângulo formado é ESCALENO')
    else:
        print('O triângulo formado é ISÓSCELES')
else:
    print('As retas não formam um triangulo!')
