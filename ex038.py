#Read two int numbers and tell which is: The first value is bigger      The second value is bigger      none value is bigger, the both is equal
n1 = int(input('Digit a number: '))
n2 = int(input('Digit another number: '))
if n1 > n2:
    print('\033[32mThe first number {} is bigger than the second number {}'.format(n1, n2))
elif n1 < n2:
    print('\033[32mThe second number {} is bigger than the first number {}'.format(n2, n1))
else:
    print('\033[36mThe numbers {} and {} are equal'.format(n1, n2))