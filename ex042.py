#remake the ex035 increasing what type of triangle it is:   Equilateral: all sides equal;    Isosceles: 2 sides equal;  Scalane: all different;
number1 = int(input('Enter the first line length: '))
number2 = int(input('Enter the second line length: '))
number3 = int(input('Enter a third line length: '))
bigger_number = number1

if number2 > bigger_number:
    bigger_number = number2

if number3 > bigger_number:
    bigger_number = number3

if bigger_number == number1:
    if bigger_number < number2 + number3:
        if number2 == number3 == bigger_number:
            print('Its possible!! This is a Equilateral triangle')
        elif bigger_number == number2 != number3 or bigger_number == number3 != number2 or bigger_number != number2 == number3:
            print('Its possible!! This is a Isosceles triangle')
        else:
            print('Its possible!! This is a Scalene triangle')
    else:
        print('Its impossible to make a triangle')
elif bigger_number == number2:
    if bigger_number < number1 + number3:
        if number1 == number3 == bigger_number:
            print('Its possible!! This is a Equilateral triangle')
        elif bigger_number == number1 != number3 or bigger_number == number3 != number1 or bigger_number != number1 == number3:
            print('Its possible!! This is a Isosceles triangle')
        else:
            print('Its possible!! This is a Scalene triangle')
    else:
        print('Its impossible to make a triangle')
elif bigger_number == number3:
    if bigger_number < number1 + number2:
        if number1 == number2 == bigger_number:
            print('Its possible!! This is a Equilateral triangle')
        elif bigger_number == number1 != number2 or bigger_number == number2 != number1 or bigger_number != number2 == number1:
            print('Its possible!! This is a Isosceles triangle')
        else:
            print('Its possible!! This is a Scalene triangle')
    else:
        print('Its impossible to make a triangle')