#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado
n=float(input('Quantos km foi percorridos com esse carro alugado?'))
s=int(input('E por quantos dias esse carro ficou alugado?'))
d=(60*s)+(0.15*n)
print('De acordo com os km percorridos e seus dias com o caror alugado,o valor do aluguel ficou no total de R${:.2f}'.format(d))
