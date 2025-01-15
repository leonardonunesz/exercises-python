# make a program that reads an angle and show the value of sin cos and tan from this angle
import math

angle = float(input('Digit the angle: '))
cos = math.cos(math.radians(angle))
sin = math.sin(math.radians(angle))
tan = math.tan(math.radians(angle))
print('The angle is: {:.0f}º\nThe cosine is: {:.2f}\nThe sino is: {:.2f}\nThe tangent is: {:.2f}'.format(angle, cos, sin, tan))