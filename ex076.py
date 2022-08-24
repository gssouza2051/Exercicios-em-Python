'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
 na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''
listagem= ('lápis',2.50,
           'borracha',1.50,
           'caderno',12.00,
           'caneta',2.00,
           'estojo',10.50)
print('-'*30)
print('LISTAGEM DE PREÇOS')
print('-'*30)
for pos in range(0, len (listagem)):
    if pos % 2==0 :
        print(f'{listagem[pos]:.<30}')
    else:
        print(f' R${listagem[pos]:>10}')
