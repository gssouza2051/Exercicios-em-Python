#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados
n=float(input('Digite a largura da parede em metros :'))
s=float(input('Agora digite a altura da parede em metros : '))
a=n*s
p=a/2
print('A área da parede é de {} m² \n e a quantidade de tinta necessária para essa área total é de {} litros de tinta'.format(a,p))

