'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO'''
n1=float(input('Digite a sua nota na primeira unidade:'))
n2=float(input('Digite a sua nota na segunda unidade:'))
m=(n1+n2)/2
if m<5:
    print('Infelizmente você foi REPROVADO!')
elif 7 > m >=5:
    print('Você está na RECUPERAÇÃO!')
elif m>=7:
    print('Você foi APROVADO!')