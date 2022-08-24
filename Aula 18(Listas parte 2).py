'''As listas são variáveis compostas que permitem armazenar
 vários valores em uma mesma estrutura, acessíveis por chaves individuais.'''
'''teste=[]
teste.append('gustavo')
teste.append(40)
galera=[]
galera.append(teste[:])
teste[0]='Maria'
teste[1]=19
galera.append(teste[:])
print(galera)'''


'''galera=[['joao',10],['gabriel',20],['rosana',17],['vitor',15]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade!')'''


galera=list()
dado=list()
totmai=totmen=0
for p in range (0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21 :
        print(f'{p[0]} é maior de idade.')
        totmai +=1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen +=1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')