nome=str(input('Qual é seu nome ?')).capitalize()
if nome == 'Gustavo':
    print('Que belo nome {}!'.format(nome))
elif nome=='Maria' or nome=='Rosana':
    print('Que belo nome feminino o seu hein {} ?'.format(nome))
else:
    print('Seu nome é raro aqui no brasil  hein {}!'.format(nome))

print('Tenha um ótimo dia, {}!'.format(nome))