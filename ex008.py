#escreva um programa que calcule o valor em metros e o exiba convertido em centimetros e milimetros
n = float(input("Enter a number in meters: "))
cm = n * 100
mm = n * 1000
print('The entered number is: {:.2f}\nIn centimeters is {:.2f}\nIn milimeters is {:.2f}'.format(n, cm, mm))