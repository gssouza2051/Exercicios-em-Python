''' Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''
nome=str(input('Digite seu nome todo :')).strip().upper()
print('seu nome tem : {} letras A'.format(nome.count('A')))
print('a primeira letra A aparece  na posição : {}'.format(nome.find('A')+1))
print('a letra A aparece na ultima vez na posição : {}'.format(nome.rfind('A')+1))