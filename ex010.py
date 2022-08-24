#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
n=float(input('Quantos reais voce tem na carteira?'))
s=n/5.51
print('com a quantidade de {} reais que voce tem,voce tem {:.2f} dólares atualmente'.format(n,s))
