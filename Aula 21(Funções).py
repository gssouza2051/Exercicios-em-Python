'''def função():
    n1=4
    print(f'N1 dentro vale {n1}')


n1=2
função()
print(f'N1 vale {n1}')'''
def par(n=0):
    if n% 2 ==0:
        return True
    else:
        return False


num=int(input('Digite um número: '))
if par(num):
    print('É PAR!')
else:
    print('NÃO')