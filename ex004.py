#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
n=input('Digite alguma coisa:')
print('o tipo primitivo desse valor é:',type(n))
print('só tem espaço?', n.isspace())
print('só tem número?',n.isnumeric())
print('só tem letra?',n.isalpha())
print('só tem letra minúscula?',n.islower())

