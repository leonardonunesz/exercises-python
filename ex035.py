#Make a program that reads the length of three lines, and show if it can make a triangle or not

number1 = float(input("Enter the first line length: "))
number2 = float(input("Enter the second line length: "))
number3 = float(input("Enter the third line length: "))
bigger_number = number1

# Verify if number2 is bigger
if number2 > bigger_number:
    bigger_number = number2
# verify if number3 is bigger
if number3 > bigger_number:
    bigger_number = number3

if bigger_number == number1:
    if bigger_number < number2 + number3:
        print('Its possible!')
    else:
        print('Its impossible!')
elif bigger_number == number2:
    if bigger_number < number1 + number3:
        print('Its possible!')
    else:
        print('Its impossible!')
else:
    if bigger_number < number1 + number2:
        print('Its possible!')
    else: print('Its impossible!')