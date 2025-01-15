#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#Considere US$1,00 = R$3,27
real = float(input('How much reais do you have in your pocket: '))
dolar = real // 3.27
print('If you have in your pocket: {:.2f} reais\nYou can buy {:.2f} dollars.'.format(real, dolar))