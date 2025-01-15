#make a program that reads the length of the opposite leg and adjacent leg of a triangle rectangle, calculate and show the length of hypotenuse
import math

co = float(input('Digit the opposite leg: '))
ca = float(input('Digit the adjacent leg: '))
coca = (math.pow(co, 2) + math.pow(ca,2))
h = math.sqrt(coca)
print('The hypotenuse is: {:.2f}'.format(h))