'''O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''
import random
n1=str(input('Digite o primeiro aluno'))
n2=str(input('Digite o segundo aluno'))
n3=str(input('Digite o terceiro aluno'))
n4=str(input('Digite o ultimo aluno'))
lista=[n1,n2,n3,n4]
escolha=random.shuffle(lista)
print('a ordem dos alunos para a apresentação dos trabalhos foi : {} '.format(lista))