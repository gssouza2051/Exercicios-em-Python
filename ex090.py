'''Faça um programa que leia nome e média de um aluno,
 guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''
aluno={}
aluno['Nome']=str(input('Digite seu nome: '))
aluno['média']=float(input(f' Média de {aluno["Nome"]}: '))
if aluno ['média']>=7:
    aluno['situação']='aprovado'
elif 5 <= aluno['média'] <7:
    aluno['situação']= 'recuperação'
else:
    aluno['situação']= 'reprovado'

for k,v in aluno.items():
    print(f' {k} é igual a {v}')
