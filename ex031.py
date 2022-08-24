'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
 cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''
viagem=float(input('Qual a distância da sua viagem em Km?'))
valor=0.5*viagem
valor2=0.5*viagem +0.45*(viagem-200)
if viagem <=200:
    print('O valor da passagem foi de R$ {}'.format(valor))
else:
    print('O valor da sua passagem foi de R$ {}'.format(valor2))