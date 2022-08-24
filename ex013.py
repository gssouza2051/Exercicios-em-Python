#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
n=float(input('Qual o valor do seu salário atual?  R$'))
s=n*(115/100)
#ou s=n+(n*15/100)
print('O valor do seu  novo salário com aumento de 15% agora é de R${:.2f}'.format(s))