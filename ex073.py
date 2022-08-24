'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que osição está o time da Chapecoense.'''
cont= ('Atlético-MG','Flamengo','Palmeiras','fortaleza','corinthians','bragantino','fluminense',
       'América-MG','Atlético-GO','Santos','Ceará','Internacional','São Paulo',
       'Atlético-PR','Cuiabá','Juventude','Grêmio','Bahia','Sport','Chapecoense')
print(f'Os cinco primeiros times são :{cont[0:5]} ')

print(f'Os últimos colocados são {cont[16:]}')

print(f' Os times em ordem alfabética : {sorted(cont)}')

print(f' A posiçao do time da chapecoense é {cont.index("Chapecoense")+1} ')
