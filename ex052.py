#reads an int number and tells if it's a prime number
n = int(input('Digit a number: '))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[32m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')

print('\033[m\nThe number {} was divided {} times.'.format(c, total), end='')
if total == 2:
    print('\033[m\nThe number is prime.', end='')
else:
    print('\033[m\nThe number isn\'t prime.', end='')