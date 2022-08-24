''' Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''
import random
n1=str(input('Digite o primeiro aluno'))
n2=str(input('Digite o segundo aluno'))
n3=str(input('Digite o terceiro aluno'))
n4=str(input('Digite o ultimo aluno'))
lista=[n1,n2,n3,n4]
escolha=random.choice(lista)
print('o aluno sorteado para apagar o quadro foi : {} '.format(escolha))

