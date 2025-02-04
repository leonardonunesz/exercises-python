#Read 3 numbers and tell which is bigger and small
number1 = float(input('Enter a number: '))
number2 = float(input('Enter another number: '))
number3 = float(input('Enter a another number: '))
bigger_number = number1
smaller_number = number1

# Verify if number2 is bigger
if number2 > bigger_number:
    bigger_number = number2

# verify if number3 is bigger
if number3 > bigger_number:
    bigger_number = number3

# verify if number2 is smaller
if number2 < smaller_number:
    smaller_number = number2

# verify if number3 is smaller
if number3 < smaller_number:
    smaller_number = number3

print('The bigger number is {}'.format(bigger_number))
print('The smaller number is {}'.format(smaller_number))
