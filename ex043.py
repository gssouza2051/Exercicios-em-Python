'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
 calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida'''
peso=float(input('Digite seu peso(Kg) : '))
altura=float(input('Digite sua altura(m) : '))
IMC=peso/(altura*altura)
print('O IMC dessa pessoa é {:.1f}'.format(IMC))
if IMC <18.5:
    print('Seu IMC está como :Abaixo do peso ')
elif 18.5 <= IMC <25:
    print('Seu IMC está como :Peso Ideal ')
elif 25 <= IMC <30:
    print('Seu IMC está como :Sobrepeso ')
elif 30 <= IMC < 40 :
    print('Seu IMC está como :Obesidade ')
elif IMC >= 40:
    print('Seu IMC está como :Obesidade Mórbida')