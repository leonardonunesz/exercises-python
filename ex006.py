# crie um algoritmo que leia seu numero e mostre seu dobro, triplo e raiz quadrada
n1 = float(input('Enter a number: '))
d = n1 * 2
t = n1 * 3
sqr = n1 ** (1/2)
print('The number is {}\nThe double is {}\nThe triple is {}\nThe square root is {:.2f}'.format(n1, d, t, sqr))