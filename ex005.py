# ordem de precedência == primeiro o (), segundo a **, terceiro os * / // %, por ultimo os + -
#faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor

n1 = int(input('Digit a value: '))
s = n1 + 1
a = n1 - 1
print('Value entered is {} \nYour successor is {} \nYour predecessor is {}'.format(n1, s, a))