#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
n=float(input('Digite uma distância em metros'))
print('o valor da sua distância em centímetros é {:.0f} cm\n e para milímetros é {:.0f} mm'.format(n*100,n*1000))

