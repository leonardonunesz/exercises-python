#A professor wants to sort one of four students to erase the black board, make a program that helps him to choose
from random import choice

std1 = input('Name a student: ')
std2 = input('Name another student: ')
std3 = input('Name another student: ')
std4 = input('Name another student: ')

print('The chosen one is: {}'.format(choice([std1, std2, std3, std4])))