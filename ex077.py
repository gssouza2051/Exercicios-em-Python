'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''
palavras= ('programar','aprender','grátis','estudo','praticar','mercado','python','linguagem','curso','futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ',end='')
    for letra in p:
        if letra.lower() in 'aáâãeéiou':
            print(letra,end=' ')