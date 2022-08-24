#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
n=float(input('Digite o valor do preço do seu produto desejado:'))
s=n*(95/100)
print('com 5% de desconto o valor agora do seu produto é de R${:.2f}'.format(s))