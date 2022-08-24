'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
 se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou
se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
idade=int(input('Em que ano você nasceu?'))
tempo=abs(idade-2003)
print('De acordo com seu ano de nascimento:')
if idade>2003:
    print('Você precisa se alistar em {} anos ,que é o tempo dos seus 18 anos'.format(tempo))
elif idade==2003:
    print('Você está na idade certa para se alistar')
else:
    print('Já passou {} anos para você se alistar'.format(tempo))