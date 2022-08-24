'''Faça um programa que leia o sexo de uma pessoa,
 mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.'''
n=str(input('Qual seu sexo? \n digite [M/F]:')).strip().upper()
while n not in 'MmFf':
    n=int(input('dados invalidos,digite novamente seu sexo ').strip().upper())
print('sexo {} registrado com sucesso'.format(n))
