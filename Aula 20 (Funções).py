'''def soma(a,b):
    print(f' A={a} e B={b}')
    s=a+b
    print(f'A SOMA DE A+B É {s}')
soma(5,3)
soma(2,1)
soma(10,5)'''
'''def contador(*num):
    tam=len(num)
    print(f'Recebi os valores{num} e ao todo são {tam} números.')


contador(2,15)
contador(1,5,9,4)
contador(1)'''
'''def dobra(lst):
    pos=0
    while pos<len(lst):
        lst[pos] *=2
        pos +=1
valores=[1,5,6,7,4,2,]
dobra(valores)
print(valores)'''
def soma(*valores):
    s=0
    for num in valores:
        s +=num
    print(f'Somando os {valores} temos {s}')


soma(5,2)
soma(4,1,6)
