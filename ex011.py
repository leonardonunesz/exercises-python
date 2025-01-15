#faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintar
#sabendo que cada litro de tinta pinta uma área de 2m²
w = float(input('Digit the weight: '))
h = float(input('Digit the height: '))
a = w * h
ink = a / 2
print('The area of the wall is {}m²\nYou will need {}l of ink per m²'.format(a, ink))