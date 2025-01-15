#A professor wants to sort the order of your students to make the presentation, make a program that helps him to choose the order
import random

std1 = input('Name a student: ')
std2 = input('Name another student: ')
std3 = input('Name another student: ')
std4 = input('Name another student: ')

stdnts = [std1, std2, std3, std4]
random.shuffle(stdnts)

print('The order of the presentation is: \nFirst: {} \nSecond: {} \nThird: {} \nForth: {}'.format(stdnts[0], stdnts[1], stdnts[2], stdnts[3]))