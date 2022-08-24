''' Desenvolva um programa que leia seis números inteiros e mostre a
soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.'''
s=0
c=0
for c in range(1,7):
    n = int(input('Digite o {} valor:'.format(c)))
    if n % 2 ==0:
        s += n
        c += 1
print('voce informou {} numeros pares e a soma foi {}'.format(c, s))

