#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
n=float(input('Está quantos graus celsius(ºC) no momento? '))
s=(n*9/5)+32
d=n+273.15
print('Convertendo para graus Fahrenheit,a temperatura está em {:.2f} ºF \n enquanto em Kelvin a temperatura está {:.2f}K'.format(s,d))