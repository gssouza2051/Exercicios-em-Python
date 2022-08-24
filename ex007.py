#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n=float(input('Digite sua primeira nota : '))
n1=float(input('Digite sua segunda nota : '))
print('a média de suas duas notas {:.1f} e {:.1f} é {:.1f} : '.format(n,n1,(n+n1)/2))
# float pq vou ter numero com decimal e ":.1f" é pra ter 1 casal decimal apenas
