'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''
salario=float(input('Quanto você ganha por mês no seu trabalho?'))
valor=salario*0.1+salario
valor2=salario*0.15+salario
if salario<=1250:
    print('com o aumento seu salário agora é de  R${:2f}'.format(valor2))
else:
    print('com o aumento seu salário agora é de  R${:.2f}'.format(valor))